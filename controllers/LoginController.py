import bcrypt
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from services.LoginService import LoginService
from utils.auth_utils import roles_required

login_bp = Blueprint('login', __name__, url_prefix='/login')

login_service = LoginService()



@login_bp.route('/', methods=['POST'])
def login():
    data = request.get_json(silent=True) or {}
    res = login_service.login(data)
    return res


