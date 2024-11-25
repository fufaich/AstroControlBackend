import json

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.EmployeeService import EmployeeService
from utils.auth_utils import roles_required

# Создаем Blueprint
employee_bp = Blueprint('employee', __name__, url_prefix='/employees')

# Пример сервиса
employee_service = EmployeeService()

@employee_bp.route('/', methods=['GET'])
@jwt_required()
def get_employees():
    filters = request.get_json(silent=True) or {}
    current_user = get_jwt_identity()  # Это значение 'sub' из токена
    user_info = json.loads(current_user)
    if "role" not in user_info:
        return  jsonify("Error"), 405


    match user_info["role"]:
        case 'admin':
            employees = employee_service.get_employees(filters)
        case _:
            filters["id_employee"] = user_info["user_id"]

    employees = employee_service.get_employees(filters)
    return jsonify(employees), 200

@employee_bp.route('/', methods=['POST'])
@roles_required('admin')
def create_employee():
    data = request.json
    res = employee_service.add_employee(data)
    return jsonify(res), 200

@employee_bp.route('/', methods=['DELETE'])
@roles_required('admin')
def delete_employee():
    data = request.json
    res = employee_service.delete_employee(data)
    return jsonify(res), 200


@employee_bp.route('/', methods=['PUT'])
@roles_required('admin')
def update_employee():
    data = request.json
    result = employee_service.upadate_employee(data)
    if result is None:
        result = "Failed"

    return jsonify(result), 200
