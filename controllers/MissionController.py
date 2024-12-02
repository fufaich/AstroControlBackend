import json

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from services.MissionService import MissionService
from utils.auth_utils import roles_required

missions_bp = Blueprint('missions', __name__, url_prefix='/missions')

missions_service = MissionService()



@missions_bp.route('/', methods=['POST'])
@jwt_required()
def add_mission():
    data = request.get_json(silent=True) or {}
    res = missions_service.add_mission(data)
    return jsonify(res), 200

@missions_bp.route('/', methods=['GET'])
@jwt_required()
def get_mission():
    try:
        filters = request.args.to_dict()
        print(f"filters: {filters}")
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON in headers"}), 400
    res = missions_service.get_mission(filters)
    if "message" in res:
        if res["message"] == "invalid filter":
            return jsonify({"error": "Invalid filter"}), 400
    return jsonify(res), 200

@missions_bp.route('/', methods=['DELETE'])
@roles_required("admin")
def delete_mission():
    data = request.get_json(silent=True) or {}
    res = missions_service.delete_mission(data)
    return jsonify(res), 200

@missions_bp.route('/', methods=['PUT'])
@roles_required("admin")
def update_mission():
    data = request.get_json(silent=True) or {}
    res = missions_service.update_mission(data)
    return jsonify(res), 200





