from flask import request, redirect, render_template, session, Blueprint
from finance_app.utils import apology, lookup, usd, login_required
from finance_app.db import get_db

buy_blueprint = Blueprint('buy', __name__, template_folder='templates', url_prefix='')

@buy_blueprint.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        return handle_buy_post()
    else:
        return render_buy_form()

def handle_buy_post():
    db = get_db()
    symbol = request.form.get("symbol")
    shares = request.form.get("shares")
    
    lookup_result = lookup(symbol)
    
    if lookup_result is None:
        return apology("Invalid symbol", 400)
    
    cash = get_user_cash(db)
    
    if not is_valid_shares(shares) or not cash:
        return apology("Invalid input", 400)

    value = lookup_result["price"] * int(shares)
    
    if not has_enough_cash(cash, value):
        return apology("You don't have enough money to proceed", 403)

    subtract_cash(db, value)
    add_transaction(db, lookup_result, shares)
    
    return redirect("/")

def render_buy_form():
    return render_template("buy.html")

def get_user_cash(db):
    result = db.execute("SELECT cash FROM user WHERE id = ?", (int(session['user_id']),)).fetchone()
    return result[0] if result else None

def is_valid_shares(shares):
    return shares.isdigit() and int(shares) >= 1

def has_enough_cash(cash, value):
    return cash >= value

def subtract_cash(db, value):
    db.execute("UPDATE user SET cash = cash - ? WHERE id = ?", (value, int(session['user_id'])))

def add_transaction(db, lookup_result, shares):
    db.execute(
        "INSERT INTO transactions (user_id, symbol, shares, price, operation_name) VALUES (?, ?, ?, ?, ?)",
        (int(session['user_id']), lookup_result['symbol'], int(shares), lookup_result['price'], 'BUY')
    )
    db.commit()
