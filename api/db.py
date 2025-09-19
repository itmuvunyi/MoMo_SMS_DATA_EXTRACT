from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()





# # from flask_sqlalchemy import SQLAlchemy
# # from flask import Flask
# # import os

# # app = Flask(__name__)

# # # Set your PostgreSQL credentials here
# # DB_USER = 'momo_user'
# # DB_PASSWORD = 'momo_pass'
# # DB_HOST = 'localhost'
# # DB_PORT = '5432'
# # DB_NAME = 'momo_db'

# # app.config['SQLALCHEMY_DATABASE_URI'] = (
# #     f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
# # )
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # db = SQLAlchemy(app)

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
 
# db = SQLAlchemy()
 
# def create_app():
#     app = Flask(__name__)
 
#     # PostgreSQL credentials
#     DB_USER = 'postgres'
#     DB_PASSWORD = 'your_password'   # put the real password
#     DB_HOST = 'localhost'
#     DB_PORT = '5432'
#     DB_NAME = 'momo_db'
 
#     app.config['SQLALCHEMY_DATABASE_URI'] = (
#         f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
#     )
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
#     db.init_app(app)
 
#     return app