from flask import Blueprint, request, jsonify
from .db import db

system_logs_bp = Blueprint('system_logs', __name__)

@system_logs_bp.route('/system_logs', methods=['GET'])
def get_system_logs():
    db = db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM System_Logs")
    logs = cursor.fetchall()
    return jsonify(logs)

@system_logs_bp.route('/system_logs', methods=['POST'])
def create_system_log():
    data = request.json
    db = db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO System_Logs (message, level, created_at) VALUES (?, ?, ?)",
                   (data['message'], data['level'], data['created_at']))
    db.commit()
    return jsonify({'id': cursor.lastrowid}), 201

@system_logs_bp.route('/system_logs/<int:log_id>', methods=['PUT'])
def update_system_log(log_id):
    data = request.json
    db = db()
    cursor = db.cursor()
    cursor.execute("UPDATE System_Logs SET message = ?, level = ? WHERE id = ?",
                   (data['message'], data['level'], log_id))
    db.commit()
    return jsonify({'updated': cursor.rowcount})

@system_logs_bp.route('/system_logs/<int:log_id>', methods=['DELETE'])
def delete_system_log(log_id):
    db = db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM System_Logs WHERE id = ?", (log_id,))
    db.commit()
    return jsonify({'deleted': cursor.rowcount})