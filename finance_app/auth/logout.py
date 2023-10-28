from flask import Flask, request, redirect, render_template, session, Blueprint


logout_blueprint = Blueprint('logout', __name__, template_folder='templates', url_prefix='')

@logout_blueprint.route("/logout", methods=["GET", "POST"])
def logout():
    """Log user out"""

    # Forget any user_id
    # session.clear()

    # Redirect user to login form
    return redirect("/")
