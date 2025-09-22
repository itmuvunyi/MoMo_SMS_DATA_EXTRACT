from flask import Blueprint, jsonify, request

from api.config.db import db

from api.customers import Customer
 
# create a Blueprint instead of a class

controller_bp = Blueprint("controller", __name__)
 
@controller_bp.route("/", methods=["GET"])


def index():

    return jsonify({"message": "Hello Man"})

 
customers_bp = Blueprint("customers", __name__)
 
# Insert (create) new customer
@controller_bp.route("/api/register", methods=["POST"])
def create_customer():
    data = request.get_json()
    if not data:

        return jsonify({"error": "No input data provided"}), 400
 
    try:

        fullname = data["fullname"]

        phoneNumber = data["phoneNumber"]
        # customer_id = data["customer_id"]
 
        new_customer = Customer(
            # customer_id = customer_id,
            fullname=fullname,
            phoneNumber=phoneNumber,

        )
        print("here is new customer",new_customer)
        db.session.add(new_customer)

        db.session.commit()
 
        return jsonify({
            # "customer_id":123,
            "message": "Customer created successfully",

            "customer": new_customer.to_dict()

        }), 201
 
    except Exception as e:

        db.session.rollback()

        return jsonify({"error": str(e)}), 500
 