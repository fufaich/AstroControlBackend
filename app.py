import json

from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import bcrypt
import Secrets
from Entity.DatabaseEngine import DatabaseConfig, DatabaseEngine
from Entity.Employee import Employee
from utils.utils import create_db_object

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = Secrets.JWT_SECRET_KEY
jwt = JWTManager(app)

config = DatabaseConfig(
        dbname = "aero_managment",
        dbuser = Secrets.USER_FOR_BD,
        dbpassword = Secrets.PASS_FOR_BD,
        dbhost = "localhost",
        port = 5432
    )

db_engine = DatabaseEngine(config)


@app.route('/')
def home():  # put application's code here
    result = db_engine.execute_query("SELECT * FROM \"Employee\"")
    print(result)
    return result

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    if not username or not password:
        return jsonify({'message': 'Missing username or password'}), 400

    user = db_engine.get_user(username)
    if user is None:
        return jsonify({'message': 'Invalid username or password'}), 401

    user_id, pass_hash, role = user
    salt = bcrypt.gensalt()
    if not bcrypt.checkpw(password.encode('utf-8'), pass_hash.encode('utf-8')):
        return jsonify({'error': 'Invalid username or password'}), 401

    user_info = {
        "user_id" : user_id,
        "username" : username,
        "role" : role
    }
    access_token = create_access_token(identity=json.dumps(user_info)) ##TODO Доделать парсинг на выходе в словарь эти данные
    return jsonify({'access_token': access_token}), 200

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity() # Это значение 'sub' из токена
    print(current_user)
    user_info = json.loads(current_user)
    return jsonify(logged_in_as=user_info["username"]), 200

@app.route('/<string:table_name>', methods=['POST'])
def create_employee(table_name:str):
    data = request.get_json()
    try:
        object = create_db_object(table_name=table_name, data=data)
    except KeyError as e:
        return jsonify({"error": str(e)}), 400
    result = db_engine.add(object)
    return result

@app.route('/<string:table_name>', methods=['GET'])
def get_object(table_name:str):
    filters = {key: value for key, value in request.args.items()}
    result = db_engine.get(table_name, filters)
    return result

@app.route('/<string:table_name>', methods=['DELETE'])
def delete_object(table_name:str):
    primary_keys = request.get_json()

    if not primary_keys:
        return jsonify({'error': 'Primary key values are required'}), 400


    result = db_engine.delete(table_name, primary_keys)
    return result


@app.route('/table_name:str/<int:employee_id>', methods=['PUT'])
def update_object(table_name:str, employee_id: int):
    data = request.get_json()
    data['id'] = employee_id

    try:
        object = create_db_object(table_name=table_name, data=data)
    except KeyError as e:
        return jsonify({"error": str(e)}), 400

    result = db_engine.update(object)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0')
