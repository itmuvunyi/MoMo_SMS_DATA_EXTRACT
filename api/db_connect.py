from flask import Flask

from sqlalchemy import text

from .db import db   # local import
 
def create_app():

    app = Flask(__name__)
 
    # PostgreSQL connection details

    DB_USER = ""

    DB_PASSWORD = ""   # replace with actual password

    DB_HOST = ""

    DB_PORT = ""

    DB_NAME = ""
 
    app.config["SQLALCHEMY_DATABASE_URI"] = (

        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 
    db.init_app(app)
 
    # @app.route("/")

    # def index():

    #     return {"message": "✅ Flask is running and DB config is set!"}
 
    return app
 