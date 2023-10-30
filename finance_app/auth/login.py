from flask import request, redirect, render_template, session, Blueprint
from finance_app.utils import apology
from finance_app.db import get_db
from werkzeug.security import check_password_hash

login_blueprint = Blueprint('login', __name__, template_folder='templates', url_prefix='')

@login_blueprint.route("/login", methods=["GET"])
def login_page():
    """Render the login page."""
    return render_template("login.html")

@login_blueprint.route("/login", methods=["POST"])
def login_user():
    """Log the user in."""
    db = get_db()

    username = request.form.get("username")
    password = request.form.get("password")

    if not username:
        return apology("must provide username", 403)

    if not password:
        return apology("must provide password", 403)

    rows = fetch_user_by_username(db, username)

    if not rows or not check_password_hash(rows["password"], password):
        return apology("invalid username and/or password", 403)

    session["user_id"] = rows["id"]
    return redirect("/")

def fetch_user_by_username(db, username):
    return db.execute("SELECT * FROM user WHERE username = (?)", (username,)).fetchone()
