from api.config.db import db  # import db from db.py


class TransactionCategory(db.Model):
    __tablename__ = "Transaction_categories"   # matches DB
    category_id = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(30))
    
class Transaction(db.Model):
    __tablename__ = "Transactions"

    transaction_id = db.Column(db.Integer, primary_key=True)
    partyA = db.Column(db.String(120), nullable=False)
    partyB = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.Numeric(12, 2), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("Transaction_categories.category_id"), nullable=True)

  # Create tables if they don't exist
    def to_dict(self):
        return {
            # "transaction_id": self.transaction_id,
            "partyA": self.partyA,
            "partyB": self.partyB,
            "amount": self.amount,
            "category_id": self.category_id,
        }