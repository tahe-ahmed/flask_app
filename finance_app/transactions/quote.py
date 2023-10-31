from flask import request, render_template, Blueprint
from finance_app.utils import apology, lookup_iex_api, usd, login_required

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
    iex_api_data = lookup_iex_api(symbol)
    
    if iex_api_data is None:
        return apology("Invalid symbol", 400)
    
    return render_quoted_template(iex_api_data)

def render_quoted_template(iex_api_data):
    name = iex_api_data["name"]
    symbol = iex_api_data["symbol"]
    price = usd(iex_api_data["price"])
    
    return render_template("quoted.html", name=name, symbol=symbol, price=price)

def render_quote_form():
    return render_template("quote.html")
