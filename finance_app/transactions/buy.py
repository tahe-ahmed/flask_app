from flask import request, redirect, render_template, Blueprint
from finance_app.utils import apology, lookup, login_required, is_valid_shares, add_transaction, update_cash, get_user_cash
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
    shares = int(request.form.get("shares"))
    
    lookup_result = lookup(symbol)
    
    if lookup_result is None:
        return apology("Invalid symbol", 400)
    
    current_cash = get_user_cash(db)
    
    if not is_valid_shares(shares) or not current_cash:
        return apology("Invalid input", 400)

    value = lookup_result["price"] * int(shares)
    
    if not has_enough_cash(current_cash, value):
        return apology("You don't have enough money to proceed", 403)

    update_cash(db, value, "SUBTRACT")

    add_transaction(db, lookup_result['symbol'], shares, lookup_result['price'], "BUY")
    
    return redirect("/")

def render_buy_form():
    return render_template("buy.html")

def has_enough_cash(cash, value):
    return cash >= value
