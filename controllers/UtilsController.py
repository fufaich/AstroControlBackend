from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from services.CompletedTasksService import CompletedTasksService
from services.ExpirementJournalService import ExperimentJournalService
from services.UtilsService import UtilsService
from utils.auth_utils import roles_required

utils_bp = Blueprint('utils', __name__, url_prefix='/utils')

utils_service = UtilsService()


@utils_bp.route('/', methods=['GET'])
def get_resource():
    data = request.get_json(silent=True) or {}
    res = utils_service.get_collumns_table(data)
    return jsonify(res), 200






