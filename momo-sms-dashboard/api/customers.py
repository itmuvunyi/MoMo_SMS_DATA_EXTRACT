from .db import db  # import db from db.py
 
class Customer(db.Model):
    __tablename__ = "customers"
 
    customer_id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(120), unique=True, nullable=False)
 
    def to_dict(self):
        return {
            # "customer_id": self.customer_id,
            "fullname": self.fullname,
            "age": self.age,
        }
 


 # from flask import Blueprint, jsonify
# from .models import Customer

# customers_bp = Blueprint('customers', __name__)

# @customers_bp.route('/customers', methods=['GET'])
# def get_customers():
#     customers = Customer.query.all()
#     return jsonify([{
#         "customer_id": c.customer_id,
#         "fullName": c.fullName,
#         "age": c.age
#     } for c in customers])