from flask import Flask, request, redirect, render_template, session, Blueprint
from finance_app.utils import apology, lookup, usd, login_required

quote_blueprint = Blueprint('quote', __name__, template_folder='templates', url_prefix='')

@quote_blueprint.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        return handle_quote_post()
    else:
        return render_quote_form()

def handle_quote_post():
    symbol = request.form.get("symbol")
    lookup_result = lookup(symbol)
    
    if lookup_result is None:
        return apology("Invalid symbol", 400)
    
    return render_quoted_template(lookup_result)

def render_quoted_template(lookup_result):
    name = lookup_result["name"]
    symbol = lookup_result["symbol"]
    price = usd(lookup_result["price"])
    return render_template("quoted.html", name=name, symbol=symbol, price=price)

def render_quote_form():
    return render_template("quote.html")
