from flask import Blueprint, request, jsonify
from .db import db
from .schemas import TransactionSchema

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    schema = TransactionSchema()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400

    conn = db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Transactions (amount, category_id, customer_id, date) VALUES (?, ?, ?, ?)',
                   (data['amount'], data['category_id'], data['customer_id'], data['date']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Transaction created successfully'}), 201

@transactions_bp.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    conn = db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Transactions WHERE id = ?', (transaction_id,))
    transaction = cursor.fetchone()
    conn.close()

    if transaction is None:
        return jsonify({'error': 'Transaction not found'}), 404

    return jsonify(transaction)

@transactions_bp.route('/transactions/<int:transaction_id>', methods=['PUT'])
def update_transaction(transaction_id):
    data = request.get_json()
    conn = db()
    cursor = conn.cursor()
    cursor.execute('UPDATE Transactions SET amount = ?, category_id = ?, customer_id = ?, date = ? WHERE id = ?',
                   (data['amount'], data['category_id'], data['customer_id'], data['date'], transaction_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Transaction updated successfully'})

@transactions_bp.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    conn = db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Transactions WHERE id = ?', (transaction_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Transaction deleted successfully'})