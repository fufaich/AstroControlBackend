from Entity.Resources import Resources
from database.DatabaseEngine import DatabaseEngine
from database.DatabaseConfig import DatabaseConfig

class ResourcesService:
    def __init__(self):
        # Инициализация соединения с базой данных через DatabaseEngine
        self.db_engine = DatabaseEngine(DatabaseConfig.get_config())

    def get_resources(self, filters: dict):
        """
        Получает список сотрудников с фильтрацией.
        :param filters: Словарь с фильтрами (например, {"role": "manager"}).
        :return: Список сотрудников.
        """
        resources = self.db_engine.get("Resources", filters=filters)
        return resources

    def add_resources(self, data: dict) -> str:
        """
        Добавляет ново.
        :param data: Словарь с данными сотрудника (например, {"name": "John", "role": "manager"}).
        :return: Результат добавления.
        """
        try:
            resources = Resources.from_json("Resources", data=data)
        except Exception as e:
            return "Add failed"

        return self.db_engine.add(resources)

    def delete_resources(self, data: dict):
        """
        Удаляет сотрудника по его ID.
        :param data:
        :param employee_id: Идентификатор сотрудника.
        :return: Результат удаления.
        """
        self.db_engine.delete("Resources", data)
        return "delete_resources"

    def update_resources(self, data: dict):
        """
        Удаляет сотрудника по его ID.
        :param employee_id: Идентификатор сотрудника.
        :return: Результат удаления.
        """
        try:
            resources = Resources.from_json_for_update("Resources", data=data)
        except Exception as e:
            return None

        res = self.db_engine.update(resources)
        return res


