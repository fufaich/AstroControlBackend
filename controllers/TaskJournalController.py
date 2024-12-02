import json

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
    try:
        filters = request.args.to_dict()
        print(f"filters: {filters}")
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON in headers"}), 400
    res = task_journal_service.get_task(filters)
    if "message" in res:
        if res["message"] == "invalid filter":
            return jsonify({"error": "Invalid filter"}), 400
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





