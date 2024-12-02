import json
from functools import wraps

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, get_jwt_identity
import bcrypt
from controllers import blueprints
app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = "2a8d3abf7bf3aee1e35b36efc59b8fb6206cff4607b6eda5f386931a45cdd45a"
jwt = JWTManager(app)

for bp in blueprints:
    app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
