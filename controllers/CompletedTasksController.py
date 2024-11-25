from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from services.CompletedTasksService import CompletedTasksService
from services.ExpirementJournalService import ExperimentJournalService
from utils.auth_utils import roles_required

completed_tasks_bp = Blueprint('completed_tasks', __name__, url_prefix='/completed_tasks')

completed_tasks_service = CompletedTasksService()



@completed_tasks_bp.route('/', methods=['POST'])
@jwt_required()
def add_resource():
    data = request.get_json(silent=True) or {}
    res = completed_tasks_service.update_tasks(data)
    return jsonify(res), 200

@completed_tasks_bp.route('/', methods=['GET'])
@roles_required("admin")
def get_resource():
    data = request.get_json(silent=True) or {}
    res = completed_tasks_service.update_tasks(data)
    return jsonify(res), 200

@completed_tasks_bp.route('/', methods=['DELETE'])
@roles_required("admin")
def delete_resource():
    data = request.get_json(silent=True) or {}
    res = completed_tasks_service.update_tasks(data)
    return jsonify(res), 200

@completed_tasks_bp.route('/', methods=['PUT'])
@roles_required("admin")
def update_resource():
    data = request.get_json(silent=True) or {}
    res = completed_tasks_service.update_tasks(data)
    return jsonify(res), 200





