import json
from functools import wraps

from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity


def roles_required(*required_roles):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            current_user = get_jwt_identity()  # Это значение 'sub' из токена
            user_info = json.loads(current_user)
            if user_info['role'] not in required_roles:
                return jsonify({"msg": f"Access forbidden: Requires one of roles {required_roles}"}), 403

            return fn(*args, **kwargs)
        return wrapper
    return decorator

