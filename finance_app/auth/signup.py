from flask import Flask, request, redirect, render_template, session, Blueprint


signup_blueprint = Blueprint('signup', __name__, template_folder='templates', url_prefix='')

@signup_blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")