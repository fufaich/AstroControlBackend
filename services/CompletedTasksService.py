from Entity.CompletedTasks import CompletedTasks
from database.DatabaseEngine import DatabaseEngine
from database.DatabaseConfig import DatabaseConfig

class CompletedTasksService:
    def __init__(self):
        # Инициализация соединения с базой данных через DatabaseEngine
        self.db_engine = DatabaseEngine(DatabaseConfig.get_config())

    def get_tasks(self, filters: dict):
        """
        Получает список сотрудников с фильтрацией.
        :param filters: Словарь с фильтрами (например, {"role": "manager"}).
        :return: Список сотрудников.
        """
        tasks = self.db_engine.get("CompletedTasks", filters=filters)
        return tasks

    def add_tasks(self, data: dict) -> str:
        """
        Добавляет ново.
        :param data: Словарь с данными сотрудника (например, {"name": "John", "role": "manager"}).
        :return: Результат добавления.
        """
        try:
            tasks = CompletedTasks.from_json("CompletedTasks", data=data)
        except Exception as e:
            return f"Add failed: {e}"

        return self.db_engine.add(tasks)

    def delete_tasks(self, data: dict):
        """
        Удаляет сотрудника по его ID.
        :param data:
        :param employee_id: Идентификатор сотрудника.
        :return: Результат удаления.
        """
        self.db_engine.delete("CompletedTasks", data)
        return "delete_resources"

    def update_tasks(self, data: dict):
        """
        Удаляет сотрудника по его ID.
        :param employee_id: Идентификатор сотрудника.
        :return: Результат удаления.
        """
        try:
            tasks = CompletedTasks.from_json_for_update("CompletedTasks", data=data)
        except Exception as e:
            return None

        res = self.db_engine.update(tasks)
        return res


