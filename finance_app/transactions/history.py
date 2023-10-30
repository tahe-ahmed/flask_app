from flask import render_template, session, Blueprint
from finance_app.utils import login_required
from finance_app.db import get_db

history_blueprint = Blueprint('history', __name__, template_folder='templates', url_prefix='')

@history_blueprint.route("/history")
@login_required
def history():
    db = get_db()
    user_id = int(session['user_id'])

    transaction_history = get_transaction_history(db, user_id)

    return render_template("history.html", stocks=transaction_history)

def get_transaction_history(db, user_id):
    query = "SELECT * FROM transactions WHERE user_id = ?"
    return db.execute(query, (user_id,)).fetchall()


