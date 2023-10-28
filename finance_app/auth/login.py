
from flask import Flask, request, redirect, render_template, session, Blueprint
from finance_app.utils import apology, clear_session
from finance_app.db import get_db

def login_page():
    """Render the login page."""
    return render_template("login.html")

def login_user():
    """Log the user in."""
    db = get_db()

    username = request.form.get("username")
    password = request.form.get("password")

    if not username:
        return apology("must provide username", 403)

    if not password:
        return apology("must provide password", 403)

    rows = db.execute("SELECT * FROM user WHERE username = (?)", (username,)).fetchone()

    if not rows or rows["password"] != password:
        return apology("invalid username and/or password", 403)

    session["user_id"] = rows["id"]
    return redirect("/")



login_blueprint = Blueprint('login', __name__, template_folder='templates', url_prefix='')

login_blueprint.route("/login", methods=["GET"])(login_page)
login_blueprint.route("/login", methods=["GET", "POST"])(login_user)
