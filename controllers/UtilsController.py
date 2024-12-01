from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from services.CompletedTasksService import CompletedTasksService
from services.ExpirementJournalService import ExperimentJournalService
from services.UtilsService import UtilsService
from utils.auth_utils import roles_required

utils_bp = Blueprint('utils', __name__, url_prefix='/utils')

utils_service = UtilsService()


@utils_bp.route('/<string:table_name>', methods=['GET'])
@jwt_required()
def get_resource(table_name: str):
    res = utils_service.get_collumns_table(table_name)
    return jsonify(res), 200






