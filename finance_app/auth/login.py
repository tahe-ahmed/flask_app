
from flask import Flask, request, redirect, render_template, session, Blueprint


login_blueprint = Blueprint('login', __name__, template_folder='templates', url_prefix='')

@login_blueprint.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")