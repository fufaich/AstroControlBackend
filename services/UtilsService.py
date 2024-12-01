import json

import bcrypt
from flask import jsonify

from database.DatabaseConfig import DatabaseConfig
from database.DatabaseEngine import DatabaseEngine


class UtilsService:
    def __init__(self):
        self.db_engine = DatabaseEngine(DatabaseConfig.get_config())


    def get_collumns_table(self, table_name:dict):
        if "name" not in table_name:
            return "Requered 'name' : table_name"

        employees = self.db_engine.get_collumns_name(table_name["name"])
        return employees

