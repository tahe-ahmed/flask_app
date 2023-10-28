from flask import Flask, request, redirect, render_template, session, Blueprint
from finance_app.utils import apology, clear_session


logout_blueprint = Blueprint('logout', __name__, template_folder='templates', url_prefix='')

@logout_blueprint.route("/logout", methods=["GET", "POST"])
def logout():
    """Log user out"""
    clear_session()

    # Redirect user to login form
    return redirect("/")
