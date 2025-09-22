from flask import Blueprint, jsonify, request

from api.config.db import db

from api.customers import Customer
from api.transaction import Transaction
 
# create a Blueprint instead of a class

# controller_bp = Blueprint("controller", __name__)
 
# @controller_bp.route("/", methods=["GET"])


# def index():

#     return jsonify({"message": "Hello Man"})

transaction_bp = Blueprint("transactions", __name__)

# Insert (create) new transaction
@transaction_bp.route("/api/transactions", methods=["POST"])
def create_transaction():
    data = request.get_json()
    if not data:

        return jsonify({"error": "No input data provided"}), 400
 
    try:

        # fullname = data["fullname"]

        # phoneNumber = data["phoneNumber"]
        # customer_id = data["customer_id"]
 
        new_transaction = Transaction(
            partyA=data["partyA"],
            partyB=data["partyB"],
            amount=data["amount"],
            category_id=data["category_id"]  # Use .get() to avoid KeyError if not provided
        )
        print("here is new transaction", new_transaction)
        db.session.add(new_transaction)

        db.session.commit()
 
        return jsonify({
            # "customer_id":123,
            "message": "Transaction created successfully",

            "transaction": new_transaction.to_dict()

        }), 201
 
    except Exception as e:

        db.session.rollback()

        return jsonify({"errorx": str(e)}), 500
