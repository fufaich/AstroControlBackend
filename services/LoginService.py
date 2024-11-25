import json

import bcrypt
from flask import jsonify
from flask_jwt_extended import create_access_token

from database.DatabaseConfig import DatabaseConfig
from database.DatabaseEngine import DatabaseEngine


class LoginService:
    def __init__(self):
        # Инициализация соединения с базой данных через DatabaseEngine
        self.db_engine = DatabaseEngine(DatabaseConfig.get_config())

    def login(self,data:dict):
        username = data['username']
        password = data['password']

        if not username or not password:
            return jsonify({'message': 'Missing username or password'}), 400

        user = self.db_engine.get_user(username)
        if user is None:
            return jsonify({'message': 'Invalid username or password'}), 401

        user_id, pass_hash, role = user
        salt = bcrypt.gensalt()
        if not bcrypt.checkpw(password.encode('utf-8'), pass_hash.encode('utf-8')):
            return jsonify({'error': 'Invalid username or password'}), 401

        user_info = {
            "user_id": user_id,
            "username": username,
            "role": role
        }
        access_token = create_access_token(identity=json.dumps(user_info))
        return jsonify({'access_token': access_token})
