from api.db import db

class Customer(db.Model):
    __tablename__ = 'customers'
    customer_id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
