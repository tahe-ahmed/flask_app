from flask import Flask, request, redirect, render_template, session, Blueprint


index_blueprint = Blueprint('index', __name__, template_folder='templates', url_prefix='')

@index_blueprint.route("/", methods=["GET", "POST"])
def index():
    """Log user out"""

    # Forget any user_id
    # session.clear()

    # Redirect user to login form
    return render_template("index.html")
