from datetime import datetime
import psycopg2
from flask import jsonify
from psycopg2 import OperationalError
from contextlib import contextmanager
from typing import Optional

from Entity.DbObject import DbObject
from utils.utils import get_str_attributes, get_str_values


# Класс для конфигурации базы данных
class DatabaseConfig:
    def __init__(self, dbname: str, dbuser: str, dbpassword: str, dbhost: str, port: int):
        self.dbname = dbname
        self.dbuser = dbuser
        self.dbpassword = dbpassword
        self.dbhost = dbhost
        self.port = port

    def as_dict(self) -> dict:
        """Возвращает конфигурацию в виде словаря."""
        return {
            'dbname': self.dbname,
            'user': self.dbuser,
            'password': self.dbpassword,
            'host': self.dbhost,
            'port': self.port
        }

def get_db_connection(config: DatabaseConfig) -> Optional[psycopg2.connect]:
    """Контекстный менеджер для работы с подключением к базе данных."""
    conn = psycopg2.connect(**config.as_dict())
    return conn


class DatabaseEngine:
    def __init__(self, config: DatabaseConfig):
        self.config = config

    def execute_query(self, query: str):
        """Пример метода для выполнения SQL-запросов."""
        conn = get_db_connection(self.config)
        if conn is None:
            return -1
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()

    def add(self, db_object: DbObject):
        if db_object.table_name is None:
            return -1 #TODO Доделать вывод ошибки
        list_attributes, list_values = db_object.get_attributes()
        str_attributes = get_str_attributes(list_attributes)
        str_values = get_str_values(list_values)

        sql_query = f"INSERT INTO \"{db_object.table_name}\" ({str_attributes}) VALUES ({str_values}) RETURNING *"

        conn = get_db_connection(self.config)
        if conn is None:
            return -1
        cur = conn.cursor()
        try:
            cur.execute(sql_query)
            user_id = cur.fetchone()[0]
            conn.commit()
            message = {'message': f'Add user success', 'id': str(user_id)}
            status = 201
        except psycopg2.IntegrityError:
            conn.rollback()
            message = {'error': 'Duplicate'}
            status = 400
        finally:
            cur.close()
            conn.close()

        return jsonify(message), status

    def get(self, table_name: str, filters: dict):

        query = f"SELECT * FROM \"{table_name}\" WHERE TRUE"
        filter_values = []

        if filters:
            for column, value in filters.items():
                query += f" AND {column} ILIKE %s"  # Используем ILIKE для нечувствительности к регистру
                filter_values.append(f"%{value}%")

        conn = get_db_connection(self.config)
        cur = conn.cursor()
        try:
            cur.execute(query, filter_values)
            data = cur.fetchall()
        except Exception:
            conn.rollback()
            data = {'message': 'invalid filter'}
        finally:
            cur.close()
            conn.close()

        return data