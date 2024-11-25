import bcrypt
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from services.LoginService import LoginService
from services.UserService import UsersService
from utils.auth_utils import roles_required

# Создаем Blueprint
users_bp = Blueprint('users', __name__, url_prefix='/users')

# Пример сервиса
users_service = UsersService()



@users_bp.route('/', methods=['POST'])
@roles_required('admin')
def add_user():
    data = request.json
    res = users_service.add_user(data)
    return res

@users_bp.route('/', methods=['GET'])
@roles_required('admin')
def get_users():
    filters = request.get_json(silent=True) or {}

    employees = users_service.get_users(filters)
    return jsonify(employees)


@users_bp.route('/', methods=['DELETE'])
@roles_required('admin')
def delete_user():
    data = request.json
    res = users_service.delete_user(data)
    return res


@users_bp.route('/', methods=['PUT'])
@roles_required('admin')
def update_user():
    data = request.json
    res = users_service.update_user(data)
    return jsonify(res), 200


