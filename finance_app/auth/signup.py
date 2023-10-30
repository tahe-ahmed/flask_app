from flask import request, redirect, render_template, session, Blueprint
from finance_app.utils import apology
from finance_app.db import get_db
from werkzeug.security import generate_password_hash

signup_blueprint = Blueprint('signup', __name__, template_folder='templates', url_prefix='')

@signup_blueprint.route("/signup", methods=["GET"])
def signup_page():
    """Render the signup page."""
    return render_template("signup.html")

@signup_blueprint.route("/signup", methods=["POST"])
def signup_user():
    """Register a new user."""
    db = get_db()

    username = request.form.get("username")
    password = request.form.get("password")

    if not username:
        return apology("must provide username", 400)

    if not password:
        return apology("must provide password", 400)

    confirmation = request.form.get("confirmation")

    if password != confirmation:
        return apology("your passwords don't match", 400)

    try:
        insert_new_user(db, username, password)
    except Exception as e:
        print("exception ", e)
        return apology("username unavailable", 400)

    rows = fetch_user_by_username(db, username)
    session["user_id"] = rows["id"]
    return redirect("/")

def insert_new_user(db, username, password):
    db.execute(
        "INSERT INTO user (email, username, password) VALUES (?, ?, ?)",
        ("test@gmail.com", username, generate_password_hash(password))
    )
    db.commit()

def fetch_user_by_username(db, username):
    return db.execute("SELECT * FROM user WHERE username = (?)", (username,)).fetchone()
