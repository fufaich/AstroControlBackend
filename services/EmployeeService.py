from flask import jsonify

from Entity.Employee import Employee
from database.DatabaseEngine import DatabaseEngine
from database.DatabaseConfig import DatabaseConfig

class EmployeeService:
    def __init__(self):
        # Инициализация соединения с базой данных через DatabaseEngine
        self.db_engine = DatabaseEngine(DatabaseConfig.get_config())

    def get_employees(self, filters: dict):
        """
        Получает список сотрудников с фильтрацией.
        :param filters: Словарь с фильтрами (например, {"role": "manager"}).
        :return: Список сотрудников.
        """
        employees = self.db_engine.get("Employee", filters=filters)
        return employees

    def add_employee(self, data: dict):
        """
        Добавляет нового сотрудника.
        :param data: Словарь с данными сотрудника (например, {"name": "John", "role": "manager"}).
        :return: Результат добавления.
        """

        employee = Employee.from_json(data=data)
        print(employee)


        return self.db_engine.add(employee)

    def delete_employee(self, data: dict):
        """
        Удаляет сотрудника по его ID.
        :param employee_id: Идентификатор сотрудника.
        :return: Результат удаления.
        """
        self.db_engine.delete("Employee", data)
        return "delete_employee"

    def upadate_employee(self, data: dict):
        """
        Удаляет сотрудника по его ID.
        :param employee_id: Идентификатор сотрудника.
        :return: Результат удаления.
        """
        return "upadate_employee"

