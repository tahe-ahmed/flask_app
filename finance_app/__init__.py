import os
from flask import Flask
from flask_session import Session
from finance_app.auth import login, logout, signup
from finance_app.home import index
from finance_app.db import init_app
from finance_app.quote import quote
from finance_app.transactions import buy, history

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    configure_app(app, test_config)
    configure_session(app)
    register_blueprints(app)
    return app

def configure_app(app, test_config):
    # Configure the app using environment variables or defaults
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'flask_app.sqlite'),
    )
    
    # if test_config is not None:
    #     # Load test configuration if provided
    #     app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize the database
    init_app(app)

def configure_session(app):
    # Configure session to use filesystem (instead of signed cookies)
    # becasue heroku has filesystem that is ephermeral we can't store the session in temp dirctory 
    # i will leave it to the default , storing it in the flass-session dirctory .
    # app.config["SESSION_FILE_DIR"] = mkdtemp()
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

def register_blueprints(app):
    app.register_blueprint(login.login_blueprint)
    app.register_blueprint(logout.logout_blueprint)
    app.register_blueprint(signup.signup_blueprint)
    app.register_blueprint(quote.quote_blueprint)
    app.register_blueprint(buy.buy_blueprint)
    app.register_blueprint(history.history_blueprint)
    app.register_blueprint(index.portfolio_blueprint)

if __name__ == "__main__":
    app = create_app()
    app.run()
