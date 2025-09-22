from flask import Flask

from sqlalchemy import text

from .db import db   # local import
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def create_app():

    app = Flask(__name__)
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_PORT= os.getenv("DB_PORT")
    # PostgreSQL connection details

    # DB_USER = "alu_assignment"

    # # DB_PASSWORD = "Shad1@123"   # replace with actual password
    # DB_PASSWORD = "Shad1%40123"   # %40 = encoded "@"

    # DB_HOST = "127.0.0.1"

    # DB_PORT = "3306"

    # DB_NAME = "assignment"
 
    app.config["SQLALCHEMY_DATABASE_URI"] = (

        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 
    db.init_app(app)
    return app
 