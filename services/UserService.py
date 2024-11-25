import json

import bcrypt
from flask import jsonify

from Entity.User import User
from database.DatabaseConfig import DatabaseConfig
from database.DatabaseEngine import DatabaseEngine


class UsersService:
    def __init__(self):
        self.db_engine = DatabaseEngine(DatabaseConfig.get_config())

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    def add_user(self,data:dict):
        res = "User added successfully"
        try:
            user_obj = User.from_json("users", data)
        except Exception as e:
            message = f"Error. Bad parameters: {e}"
            return jsonify(message), 405

        password_hash = self.hash_password(user_obj.pass_hash)
        user_obj.pass_hash = password_hash

        res = self.db_engine.add(user_obj)
        return res[0], res[1]

    def delete_user(self, data):
        res = "User deleted successfully"
        id = None
        if "id_user" in data:
            id = data["id_user"]
        else:
            return jsonify("Bad request. Requere id_user: int"), 405


        res = self.db_engine.delete("users", {"id_user": id})
        return jsonify(res), 200

    def get_users(self, filters):
        employees = self.db_engine.get("users", filters=filters)
        return employees

    def update_user(self, data):
        user = User.from_json_for_update("users", data)
        res = self.db_engine.update(user)
        return res
