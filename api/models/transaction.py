from api.db import db

class Transaction(db.Model):
    __tablename__ = 'transactions'
    transaction_id = db.Column(db.Integer, primary_key=True)
    partyA = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    transaction_date = db.Column(db.DateTime, server_default=db.func.now())
    partyB = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    amount = db.Column(db.Numeric(12,2), nullable=False)
