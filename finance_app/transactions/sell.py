from flask import request, redirect, render_template, session, Blueprint
from finance_app.utils import apology, login_required, get_current_stock_info, update_cash, has_enough_shares, add_transaction
from finance_app.db import get_db

sell_blueprint = Blueprint('sell', __name__, template_folder='templates', url_prefix='')

@sell_blueprint.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        return handle_sell_post()
    else:
        return render_sell_form()

def handle_sell_post():
    
    db = get_db()
    symbol = request.form.get("symbol")
    shares = int(request.form.get("shares"))
        
    price, available_shares = get_current_stock_info(db, symbol)
            
    if not has_enough_shares(shares, available_shares):
        return apology("you want to sell more shares than you have")
        
    total_shares_price = price * shares
    
    update_cash(db, total_shares_price, "ADD")

    add_transaction(db, symbol, shares, price, "SELL")
    
    return redirect("/")

def render_sell_form():
    db = get_db()
    # get the current user symbols
    query = """
        SELECT symbol, shares, price
        FROM transactions
        WHERE user_id = ?
    """
    stocks = db.execute(query, (int(session['user_id']),)).fetchall()   
    
    unique_symbol_list = []

    for stock in stocks:
        if stock["symbol"] not in unique_symbol_list:
            unique_symbol_list.append(stock["symbol"])
    
    return render_template("sell.html", symbols = unique_symbol_list)
