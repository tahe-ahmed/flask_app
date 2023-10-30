from flask import Blueprint, render_template, session
from finance_app.db import get_db
from finance_app.utils import login_required, usd

portfolio_blueprint = Blueprint('portfolio', __name__, template_folder='templates', url_prefix='')

INITIAL_CASH = 10000

@portfolio_blueprint.route("/")
@login_required
def show_portfolio():
    db = get_db()

    # Retrieve buy and sell transactions
    buy_transactions = get_user_transactions(db, session['user_id'], 'BUY')
    sell_transactions = get_user_transactions(db, session['user_id'], 'SELL')

    # Calculate total holdings
    total_holdings = calculate_holdings(buy_transactions, sell_transactions)

    # Calculate available cash
    available_cash = calculate_available_cash(INITIAL_CASH, total_holdings)

    return render_template("index.html", stocks=total_holdings, available_cash=usd(available_cash), cash=usd(INITIAL_CASH))

def get_user_transactions(db, user_id, operation_name):
    query = """
        SELECT symbol, shares, price
        FROM transactions
        WHERE user_id = ? AND operation_name = ?
    """
    return db.execute(query, (user_id, operation_name)).fetchall()

def calculate_holdings(buy_transactions, sell_transactions):
    symbol_totals = {}
    
    # Calculate buy totals
    for symbol, shares, price in buy_transactions:
        if symbol not in symbol_totals:
            symbol_totals[symbol] = {'shares': 0, 'total_price': 0, 'price_per_share': price}
        symbol_totals[symbol]['shares'] += shares
        symbol_totals[symbol]['total_price'] += shares * price

    # Subtract sell totals
    for symbol, shares, price in sell_transactions:
        if symbol in symbol_totals:
            symbol_totals[symbol]['shares'] -= shares
            symbol_totals[symbol]['total_price'] -= shares * price

    # Filter out stocks with zero shares
    symbol_totals = {symbol: data for symbol, data in symbol_totals.items() if data['shares'] > 0}
    # symbol_totals.update( , total_price)
    
    for symbol_to_update in symbol_totals:
        symbol_totals[symbol_to_update]['total_price'] = usd(symbol_totals[symbol_to_update]['total_price'])
    
    return symbol_totals

def calculate_available_cash(initial_cash, holdings):
    used_cash = sum( float(data['total_price'][1:]) for data in holdings.values())
    return initial_cash - used_cash
