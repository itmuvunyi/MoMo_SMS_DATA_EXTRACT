from flask import Blueprint, request, jsonify
from .db import db

transaction_categories_bp = Blueprint('transaction_categories', __name__)

@transaction_categories_bp.route('/transaction_categories', methods=['GET'])
def get_transaction_categories():
    db = db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Transaction_categories")
    categories = cursor.fetchall()
    return jsonify(categories)

@transaction_categories_bp.route('/transaction_categories', methods=['POST'])
def create_transaction_category():
    new_category = request.json
    db = db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO Transaction_categories (name) VALUES (?)", (new_category['name'],))
    db.commit()
    return jsonify(new_category), 201

@transaction_categories_bp.route('/transaction_categories/<int:id>', methods=['PUT'])
def update_transaction_category(id):
    updated_category = request.json
    db = db()
    cursor = db.cursor()
    cursor.execute("UPDATE Transaction_categories SET name = ? WHERE id = ?", (updated_category['name'], id))
    db.commit()
    return jsonify(updated_category)

@transaction_categories_bp.route('/transaction_categories/<int:id>', methods=['DELETE'])
def delete_transaction_category(id):
    db = db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM Transaction_categories WHERE id = ?", (id,))
    db.commit()
    return '', 204