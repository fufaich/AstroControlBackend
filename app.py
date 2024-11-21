
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
    employee = Employee.from_json(table_name="Employee",data=data)
    result = db_engine.add(employee)
    print(result)
    return result

@app.route('/employee', methods=['GET'])
def get_employee():
    result = db_engine.get("Employee", None)
    return result

if __name__ == '__main__':
    app.run()
