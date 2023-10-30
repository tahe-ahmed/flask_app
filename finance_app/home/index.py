from flask import Blueprint, render_template, session
from finance_app.db import get_db
from finance_app.utils import login_required, usd

portfolio_blueprint = Blueprint('portfolio', __name__, template_folder='templates', url_prefix='')

INITIAL_CASH = 10000

@portfolio_blueprint.route("/")
@login_required
def show_portfolio():
    db = get_db()
    buy_transactions = fetch_buy_transactions(db)
    symbol_totals = calculate_holding_totals(buy_transactions)
    filtered_data = prepare_filtered_data(symbol_totals)
    cash = INITIAL_CASH
    available_cash = calculate_available_cash(cash, symbol_totals)
    return render_template("index.html", stocks=filtered_data, available_cash=usd(available_cash), cash=usd(cash))

def fetch_buy_transactions(db):
    query = """
        SELECT symbol, shares, price
        FROM transactions
        WHERE user_id = ? AND operation_name = 'BUY'
    """
    return db.execute(query, (int(session['user_id']),)).fetchall()

def calculate_holding_totals(buy_transactions):
    symbol_totals = {}
    for symbol, shares, price in buy_transactions:
        if symbol not in symbol_totals:
            symbol_totals[symbol] = {'shares': 0, 'total_price': 0}
        symbol_totals[symbol]['shares'] += shares
        symbol_totals[symbol]['total_price'] += shares * price
    return symbol_totals

def prepare_filtered_data(symbol_totals):
    return [{'symbol': symbol, 'name': symbol, 'shares': totals['shares'], 'price': usd(totals['total_price']), 'total': usd(totals['total_price'])}
            for symbol, totals in symbol_totals.items()]

def calculate_available_cash(cash, symbol_totals):
    return cash - sum(totals['total_price'] for totals in symbol_totals.values())
