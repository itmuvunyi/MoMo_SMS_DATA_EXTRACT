from api.db import db
class SystemLog(db.Model):
    __tablename__ = 'system_logs'
    log_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('transaction_categories.category_id'), nullable=False)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.transaction_id'))
    transaction_date = db.Column(db.DateTime, server_default=db.func.now())