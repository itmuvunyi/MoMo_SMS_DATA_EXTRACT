from api.config.db import db  # import db from db.py

class Customer(db.Model):
    __tablename__ = "Customers"
 
    customer_id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.String(120), unique=True, nullable=False)

  # Create tables if they don't exist
    def to_dict(self):
        return {
            # "customer_id": self.customer_id,
            "fullname": self.fullname,
            "phoneNumber": self.phoneNumber,
        }