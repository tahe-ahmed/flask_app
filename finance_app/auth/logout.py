from flask import redirect, Blueprint
from finance_app.utils import clear_session

logout_blueprint = Blueprint('logout', __name__, template_folder='templates', url_prefix='')

@logout_blueprint.route("/logout", methods=["GET", "POST"])
def logout():
    clear_session()

    return redirect("/")
