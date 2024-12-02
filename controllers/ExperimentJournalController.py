import json

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from services.ExpirementJournalService import ExperimentJournalService
from utils.auth_utils import roles_required

experiment_journal_bp = Blueprint('experiment_journal', __name__, url_prefix='/experiment_journal')

experiment_journal_service = ExperimentJournalService()



@experiment_journal_bp.route('/', methods=['POST'])
@jwt_required()
def add_resource():
    data = request.get_json(silent=True) or {}
    res = experiment_journal_service.add_experiment(data)
    return jsonify(res), 200

@experiment_journal_bp.route('/', methods=['GET'])
@jwt_required()
def get_resource():
    try:
        filters = request.args.to_dict()
        print(f"filters: {filters}")
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON in headers"}), 400
    res = experiment_journal_service.get_experiment(filters)
    if "message" in res:
        if res["message"] == "invalid filter":
            return jsonify({"error": "Invalid filter"}), 400
    return jsonify(res), 200

@experiment_journal_bp.route('/', methods=['DELETE'])
@jwt_required()
def delete_resource():
    data = request.get_json(silent=True) or {}
    res = experiment_journal_service.delete_experiment(data)
    return jsonify(res), 200

@experiment_journal_bp.route('/', methods=['PUT'])
@jwt_required()
def update_resource():
    data = request.get_json(silent=True) or {}
    res = experiment_journal_service.update_experiment(data)
    return jsonify(res), 200





