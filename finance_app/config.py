import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_KEY = getenv("API_KEY", None)

def config_db(app): 
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'flask_app.sqlite'),
    )
