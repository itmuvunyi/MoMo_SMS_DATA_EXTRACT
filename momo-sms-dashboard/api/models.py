from .db import db

class Customer(db.Model):
    __tablename__ = 'customers'
    customer_id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

class TransactionCategory(db.Model):
    __tablename__ = 'transaction_categories'
    category_id = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(30))

class Transaction(db.Model):
    __tablename__ = 'transactions'
    transaction_id = db.Column(db.Integer, primary_key=True)
    partyA = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    transaction_date = db.Column(db.DateTime, server_default=db.func.now())
    partyB = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    amount = db.Column(db.Numeric(12,2), nullable=False)

class SystemLog(db.Model):
    __tablename__ = 'system_logs'
    log_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('transaction_categories.category_id'), nullable=False)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.transaction_id'))
    transaction_date = db.Column(db.DateTime, server_default=db.func.now())