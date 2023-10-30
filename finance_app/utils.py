import requests
from flask import redirect, render_template, session
from functools import wraps
from finance_app.config import API_KEY

def clear_session():
    session.clear()

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def lookup(symbol):
    """Look up quote for symbol."""
    # Contact API
    try:
        api_key = API_KEY,
        response = requests.get(f"https://api.iex.cloud/v1/data/core/quote/{str(symbol)}?token={ list(api_key)[0]}")
        response.raise_for_status()
    except requests.RequestException as e:
        print("error : ", e)
        return None

    # Parse response
    try:
        quote = response.json()[0]
        print("quote : ", quote)
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None

def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"



def get_current_stock_info(db, symbol):
    buy_query = """
        SELECT symbol, SUM(shares) AS total_shares, price
        FROM transactions
        WHERE user_id = ? AND operation_name = 'BUY' AND symbol = ?
        GROUP BY symbol
    """
    sell_query = """
        SELECT symbol, SUM(shares) AS total_shares, price
        FROM transactions
        WHERE user_id = ? AND operation_name = 'SELL' AND symbol = ?
        GROUP BY symbol
    """
    
    buy_data = db.execute(buy_query, (int(session['user_id']), symbol)).fetchone()
    sell_data = db.execute(sell_query, (int(session['user_id']), symbol)).fetchone()

    buy_shares = buy_data["total_shares"] if buy_data else 0
    sell_shares = sell_data["total_shares"] if sell_data else 0

    available_shares = buy_shares - sell_shares
    price = buy_data["price"] if buy_data else 0

    return price, available_shares


def is_valid_shares(shares):
    return int(shares) >= 1

def has_enough_shares(shares, available_shares):
    return shares <= available_shares

def update_cash(db, value, operation_type):
    if operation_type == 'ADD':
        db.execute("UPDATE user SET cash = cash + ? WHERE id = ?", (value, int(session['user_id'])))
    elif operation_type == 'SUBTRACT':
        db.execute("UPDATE user SET cash = cash - ? WHERE id = ?", (value, int(session['user_id'])))
    db.commit()

def add_transaction(db, symbol, shares, price, operation_name):
    db.execute(
        "INSERT INTO transactions (user_id, symbol, shares, price, operation_name) VALUES (?, ?, ?, ?, ?)",
        (int(session['user_id']), symbol, shares, price, operation_name)
    )
    db.commit()

def get_user_cash(db):
    result = db.execute("SELECT cash FROM user WHERE id = ?", (int(session['user_id']),)).fetchone()
    return result[0] if result else None