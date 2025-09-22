from .config.db_connect import create_app
from sqlalchemy import text
from .config.db import db   # local import
from .controllers.controller import controller_bp   # import the blueprint
from .controllers.transactioncontroler import transaction_bp  # import the transaction blueprint

if __name__ == "__main__":
    app = create_app()
 
    # register your blueprint here
    app.register_blueprint(controller_bp)
    app.register_blueprint(transaction_bp)
 
    with app.app_context():
        try:
            # run a lightweight query to test the DB
            db.session.execute(text("SELECT 1"))
            print("✅ Database connection successful!")
        except Exception as e:
            print(" Database connection failed:", e)
 
    app.run(debug=True)