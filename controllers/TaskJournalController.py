import bcrypt
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from services.LoginService import LoginService
from services.TaskJournalService import TaskJournalService
from utils.auth_utils import roles_required

task_journal_bp = Blueprint('task_journal', __name__, url_prefix='/task_journal')

task_journal_service = TaskJournalService()



@task_journal_bp.route('/', methods=['POST'])
@jwt_required()
def add_task():
    data = request.get_json(silent=True) or {}
    res = task_journal_service.add_task(data)
    return jsonify(res), 200

@task_journal_bp.route('/', methods=['GET'])
@jwt_required()
def get_task():
    data = request.get_json(silent=True) or {}
    res = task_journal_service.get_task(data)
    return jsonify(res), 200

@task_journal_bp.route('/', methods=['DELETE'])
@jwt_required()
def delete_task():
    data = request.get_json(silent=True) or {}
    res = task_journal_service.delete_task(data)
    return jsonify(res), 200

@task_journal_bp.route('/', methods=['PUT'])
@jwt_required()
def update_task():
    data = request.get_json(silent=True) or {}
    res = task_journal_service.update_task(data)
    return jsonify(res), 200





