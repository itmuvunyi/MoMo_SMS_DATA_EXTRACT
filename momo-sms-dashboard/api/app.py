# from .db_connect import create_app

# from sqlalchemy import text

# from .db import db   # local import

# from .controller import controller
 
 
# if __name__ == "__main__":

#     app = create_app()

#     with app.app_context():

#         try:

#             # run a lightweight query to test the DB

#             db.session.execute(text("SELECT 1"))


#             print("✅ Database connection successful!")

#         except Exception as e:

#             print(" Database connection failed:", e)

#     app.run(debug=True)

 
from .db_connect import create_app
from sqlalchemy import text
from .db import db   # local import
from .controller import controller_bp   # import the blueprint
 
if __name__ == "__main__":
    app = create_app()
 
    # register your blueprint here
    app.register_blueprint(controller_bp)
 
    with app.app_context():
        try:
            # run a lightweight query to test the DB
            db.session.execute(text("SELECT 1"))
            print("✅ Database connection successful!")
        except Exception as e:
            print(" Database connection failed:", e)
 
    app.run(debug=True)