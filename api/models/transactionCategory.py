from api.db import db

class TransactionCategory(db.Model):
    # __tablename__ = 'transaction_categories'
     __tablename__ = "Transaction_categories"
    category_id = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(30))