import json

import bcrypt
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from services.LoginService import LoginService
from services.UserService import UsersService
from utils.auth_utils import roles_required

users_bp = Blueprint('users', __name__, url_prefix='/users')

users_service = UsersService()



@users_bp.route('/', methods=['POST'])
@roles_required('admin')
def add_user():
    data = request.get_json(silent=True) or {}
    res = users_service.add_user(data)
    return jsonify(res), 200

@users_bp.route('/', methods=['GET'])
@roles_required('admin')
def get_users():
    try:
        filters = request.args.to_dict()
        print(f"filters: {filters}")
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON in headers"}), 400

    employees = users_service.get_users(filters)
    if "message" in employees:
        if employees["message"] == "invalid filter":
            return jsonify({"error": "Invalid filter"}), 400
    return jsonify(employees), 200


@users_bp.route('/', methods=['DELETE'])
@roles_required('admin')
def delete_user():
    data = request.json
    res = users_service.delete_user(data)
    return jsonify(res), 200

@users_bp.route('/', methods=['PUT'])
@roles_required('admin')
def update_user():
    data = request.json
    res = users_service.update_user(data)
    return jsonify(res), 200


