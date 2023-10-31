from flask import Blueprint, render_template, session
from finance_app.db import get_db
from finance_app.utils import login_required, usd, get_user_transactions, get_user_cash

index_blueprint = Blueprint('index', __name__, template_folder='templates', url_prefix='')

TOTAL_CASH = 10000

@index_blueprint.route("/")
@login_required
def index():
    db = get_db()

    buy_transactions = get_user_transactions(db, session['user_id'], 'BUY')
    sell_transactions = get_user_transactions(db, session['user_id'], 'SELL')

    total_holdings = calculate_holdings(buy_transactions, sell_transactions)
    
    total_holdings = formate_stock_total_price(total_holdings)

    available_cash = get_user_cash(db)

    return render_template("index.html", stocks=total_holdings, available_cash=usd(available_cash), cash=usd(TOTAL_CASH))

# This is a pure function 
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

    symbol_totals = {symbol: data for symbol, data in symbol_totals.items() if data['shares'] > 0}
    
    return symbol_totals

# Is this pure function ??
def formate_stock_total_price(holdings):
    holdings_formated = holdings
    for data in holdings_formated.values():
        data['total_price'] = usd(data['total_price'])
        
    return holdings_formated