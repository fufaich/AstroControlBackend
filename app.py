
from flask import Flask, jsonify, request
import Secrets
from Entity.DatabaseEngine import DatabaseConfig, DatabaseEngine
from Entity.Employee import Employee

app = Flask(__name__)

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


@app.route('/employee', methods=['POST'])
def create_employee():
    data = request.get_json()
    try:
        employee = Employee.from_json(table_name="Employee",data=data)
    except KeyError as e:
        return jsonify({"error": str(e)}), 400
    result = db_engine.add(employee)
    print(result)
    return result

@app.route('/employee', methods=['GET'])
def get_employee():
    filters = {key: value for key, value in request.args.items()}
    result = db_engine.get("Employee", filters)
    return result

@app.route('/employee/<int:employee_id>', methods=['DELETE'])
def update_employee(employee_id):
    result = db_engine.delete("Employee", employee_id)
    return result


@app.route('/employee/<int:employee_id>', methods=['PUT'])
def delete_employee(employee_id):
    data = request.get_json()
    data['id'] = employee_id
    employee = Employee.from_json_for_update("Employee", data)
    result = db_engine.update(employee)
    return result

if __name__ == '__main__':
    app.run()
