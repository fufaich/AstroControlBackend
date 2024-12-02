import json

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from services.ReportsJournalController import ReportsJournalService
from utils.auth_utils import roles_required

reports_journal_bp = Blueprint('reports_journal', __name__, url_prefix='/reports_journal')

reports_journal_service = ReportsJournalService()



@reports_journal_bp.route('/', methods=['POST'])
@jwt_required()
def add_reports():
    data = request.get_json(silent=True) or {}
    res = reports_journal_service.add_reports(data)
    return jsonify(res), 200

@reports_journal_bp.route('/', methods=['GET'])
@jwt_required()
def get_reports():
    try:
        filters = request.args.to_dict()
        print(f"filters: {filters}")
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON in headers"}), 400
    res = reports_journal_service.get_reports(filters)
    if "message" in res:
        if res["message"] == "invalid filter":
            return jsonify({"error": "Invalid filter"}), 400
    return jsonify(res), 200

@reports_journal_bp.route('/', methods=['DELETE'])
@roles_required("admin")
def delete_reports():
    data = request.get_json(silent=True) or {}
    res = reports_journal_service.delete_reports(data)
    return jsonify(res), 200

@reports_journal_bp.route('/', methods=['PUT'])
@roles_required("admin")
def update_reports():
    data = request.get_json(silent=True) or {}
    res = reports_journal_service.update_reports(data)
    return jsonify(res), 200





