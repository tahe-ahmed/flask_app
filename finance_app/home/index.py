from flask import Blueprint, render_template, session
from finance_app.db import get_db
from finance_app.utils import login_required, lookup, usd, unique_stocks

portfolio_blueprint = Blueprint('portfolio', __name__,  template_folder='templates', url_prefix='')

@portfolio_blueprint.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    db = get_db()

    # Fetch buy stocks from transactions
    stocks = get_buy_stocks(db)

    # Calculate total holdings for each symbol
    symbol_totals = calculate_symbol_totals(stocks)

    # Create a list of dictionaries for filtered data
    filtered_data = create_filtered_data(symbol_totals)

    cash = 10000
    available_cash = calculate_available_cash(cash, symbol_totals)

    return render_template("index.html", stocks=filtered_data, available_cash=usd(available_cash), cash=usd(cash))

def get_buy_stocks(db):
    """Fetch buy stocks from transactions for the user"""
    query = """
        SELECT symbol, shares, price
        FROM transactions
        WHERE user_id = ? AND operation_name = 'BUY'
    """
    return db.execute(query, (int(session['user_id']),)).fetchall()

def calculate_symbol_totals(stocks):
    """Calculate total shares and total price for each symbol"""
    symbol_totals = {}
    for symbol, shares, price in stocks:
        if symbol not in symbol_totals:
            symbol_totals[symbol] = {'shares': 0, 'price': 0}
        symbol_totals[symbol]['shares'] += shares
        symbol_totals[symbol]['price'] += shares * price
    return symbol_totals

def create_filtered_data(symbol_totals):
    """Create a list of dictionaries for filtered data"""
    return [{'symbol': symbol, 'name': symbol, 'shares': totals['shares'], 'price': round(totals['price'], 2), 'total': round(totals['price'], 2)}
            for symbol, totals in symbol_totals.items()]

def calculate_available_cash(cash, symbol_totals):
    """Calculate available cash for the user"""
    return cash - sum(totals['price'] for totals in symbol_totals.values())
