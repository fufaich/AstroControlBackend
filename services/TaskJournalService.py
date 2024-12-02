from flask import jsonify

from Entity.Employee import Employee
from Entity.TaskJournal import TaskJournal
from database.DatabaseEngine import DatabaseEngine
from database.DatabaseConfig import DatabaseConfig

class TaskJournalService:
    def __init__(self):
        # Инициализация соединения с базой данных через DatabaseEngine
        self.db_engine = DatabaseEngine(DatabaseConfig.get_config())

    def get_task(self, filters: dict):
        """
        Получает список сотрудников с фильтрацией.
        :param filters: Словарь с фильтрами (например, {"role": "manager"}).
        :return: Список сотрудников.
        """
        tasks = self.db_engine.get("TaskJournal", filters=filters)
        return tasks

    def add_task(self, data: dict) -> str:
        """
        Добавляет ново.
        :param data: Словарь с данными сотрудника (например, {"name": "John", "role": "manager"}).
        :return: Результат добавления.
        """
        try:
            employee = TaskJournal.from_json("TaskJournal", data=data)
        except Exception as e:
            return "Add failed"

        return self.db_engine.add(employee)

    def delete_task(self, data: dict):
        """
        Удаляет сотрудника по его ID.
        :param employee_id: Идентификатор сотрудника.
        :return: Результат удаления.
        """
        self.db_engine.delete("TaskJournal", data)
        return "delete_employee"

    def update_task(self, data: dict):
        """
        Удаляет сотрудника по его ID.
        :param employee_id: Идентификатор сотрудника.
        :return: Результат удаления.
        """
        try:
            task = TaskJournal.from_json_for_update("TaskJournal", data=data)
        except Exception as e:
            return None

        res = self.db_engine.update(task)
        return res


