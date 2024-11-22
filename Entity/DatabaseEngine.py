from datetime import datetime
import psycopg2
from flask import jsonify
from psycopg2 import OperationalError
from contextlib import contextmanager
from typing import Optional

from Entity.DbObject import DbObject
from utils.utils import get_str_attributes, get_str_values, clean_dict


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

    def get_first_n_collumns_name(self, table_name:str):
        # sql_query = f"SELECT column_name FROM information_schema.columns WHERE table_name = \'{table_name}\' ORDER BY ordinal_position LIMIT {n}"



        sql_query = f"SELECT kcu.column_name FROM information_schema.table_constraints tc JOIN information_schema.key_column_usage kcu ON tc.constraint_name = kcu.constraint_name WHERE tc.table_name = \'{table_name}\' AND tc.constraint_type = 'PRIMARY KEY';"
        conn = get_db_connection(self.config)
        if conn is None:
            return -1
        cur = conn.cursor()
        result = list()
        tmpresult = []
        try:
            cur.execute(sql_query)
            tmpresult = cur.fetchall()
            conn.commit()
        except Exception as e:
            conn.rollback()
            cur.close()
            conn.close()
            return None
        finally:
            cur.close()
            conn.close()
            if len(tmpresult) != 0:
                for i in range(len(tmpresult)):
                    result.append(tmpresult[i][0])

            return result

    def add(self, db_object: DbObject):
        if db_object.table_name is None:
            return -1
        list_attributes, list_values = db_object.get_attributes()
        str_attributes = get_str_attributes(list_attributes)
        str_values = get_str_values(list_values)

        sql_query = f"INSERT INTO \"{db_object.table_name}\" ({str_attributes}) VALUES ({str_values}) RETURNING *"
        print(sql_query)
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

    def update(self, db_object: DbObject):
        if db_object.table_name is None:
            return -1
        sql_query = f"UPDATE \"{db_object.table_name}\" SET "
        dict_attributes = db_object.get_dict_attributes()
        dict_attributes = clean_dict(dict_attributes)
        for key, value in dict_attributes.items():
            sql_query+= f" \"{key}\" = \'{value}\', "

        sql_query = sql_query[:-2]
        id_collumn_name = self.get_first_n_collumns_name(db_object.table_name)
        len_pk = len(id_collumn_name)
        if len_pk == 1:
            sql_query += f" WHERE {id_collumn_name[0]} = {db_object.id}"
        else:
            sql_query += f" WHERE "
            for i in range(len_pk):
                if i == len_pk - 1:
                    sql_query += f" {id_collumn_name[i]} = \'{db_object.id}\'"
                else:
                    sql_query += f" {id_collumn_name[i]} = \'{db_object.id}\' AND "


        conn = get_db_connection(self.config)
        cur = conn.cursor()
        try:
            cur.execute(sql_query)
            conn.commit()
            message = {'message': 'Rows updated'}
            status = 200
        except Exception as e:
            conn.rollback()
            message = {'error': f'Error: {e}'}
            status = 400
        finally:
            cur.close()
            conn.close()
        return jsonify(message), status

    def delete(self, table_name:str, primary_keys: dict):
        conn = get_db_connection(self.config)
        cur = conn.cursor()

        sql_query = f"DELETE FROM \"{table_name}\" "

        id_collumn_name = self.get_first_n_collumns_name(table_name)
        len_pk = len(id_collumn_name)

        if len_pk!= len(primary_keys):
            raise ValueError("Mismatch between primary key structure and provided values")

        if len_pk == 1:
            sql_query += f" WHERE {id_collumn_name[0]} = {primary_keys[id_collumn_name[0]]}"
        else:
            sql_query += f" WHERE "
            for i in range(len_pk):
                if i == len_pk - 1:
                    sql_query += f" {id_collumn_name[i]} = \'{primary_keys[id_collumn_name[i]]}\'"
                else:
                    sql_query += f" {id_collumn_name[i]} = \'{primary_keys[id_collumn_name[i]]}\' AND "
        print(sql_query)
        try:
            cur.execute(sql_query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            message = {'error': f'Error: {e}'}
            status = 400
            return jsonify(message), status
        finally:
            cur.close()
            conn.close()
            status = 200
            return jsonify({'message': 'Row deleted!'}), status

    def get_user(self, username):
        """Возвращает None или id pass_hash role"""
        conn = get_db_connection(self.config)
        cur = conn.cursor()

        cur.execute(f"SELECT id_user, pass_hash, role FROM users WHERE username = \'{username}\'")
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user is None:
            return None
        return user[0], user[1], user[2]

