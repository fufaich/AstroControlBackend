import json

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from services.ResourceService import ResourcesService

resources_bp = Blueprint('resources', __name__, url_prefix='/resources')

resources_service = ResourcesService()



@resources_bp.route('/', methods=['POST'])
@jwt_required()
def add_resource():
    data = request.get_json(silent=True) or {}
    res = resources_service.add_resources(data)
    return jsonify(res), 200

@resources_bp.route('/', methods=['GET'])
@jwt_required()
def get_resource():
    try:
        filters = request.args.to_dict()
        print(f"filters: {filters}")
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON in headers"}), 400
    res = resources_service.get_resources(filters)
    if "message" in res:
        if res["message"] == "invalid filter":
            return jsonify({"error": "Invalid filter"}), 400
    return jsonify(res), 200

@resources_bp.route('/', methods=['DELETE'])
@jwt_required()
def delete_resource():
    data = request.get_json(silent=True) or {}
    res = resources_service.delete_resources(data)
    return jsonify(res), 200

@resources_bp.route('/', methods=['PUT'])
@jwt_required()
def update_resource():
    data = request.get_json(silent=True) or {}
    res = resources_service.update_resources(data)
    return jsonify(res), 200





