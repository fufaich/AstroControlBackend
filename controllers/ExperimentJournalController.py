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
    data = request.get_json(silent=True) or {}
    res = experiment_journal_service.get_experiment(data)
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





