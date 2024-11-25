from Entity.Mission import Mission
from database.DatabaseEngine import DatabaseEngine
from database.DatabaseConfig import DatabaseConfig

class MissionService:
    def __init__(self):
        # Инициализация соединения с базой данных через DatabaseEngine
        self.db_engine = DatabaseEngine(DatabaseConfig.get_config())

    def get_mission(self, filters: dict):
        """
        Получает список сотрудников с фильтрацией.
        :param filters: Словарь с фильтрами (например, {"role": "manager"}).
        :return: Список сотрудников.
        """
        mission = self.db_engine.get("Mission", filters=filters)
        return mission

    def add_mission(self, data: dict) -> str:
        """
        Добавляет ново.
        :param data: Словарь с данными сотрудника (например, {"name": "John", "role": "manager"}).
        :return: Результат добавления.
        """
        try:
            mission = Mission.from_json("Mission", data=data)
        except Exception as e:
            return "Add failed"

        return self.db_engine.add(mission)

    def delete_mission(self, data: dict):
        """
        Удаляет сотрудника по его ID.
        :param data:
        :param employee_id: Идентификатор сотрудника.
        :return: Результат удаления.
        """
        self.db_engine.delete("Mission", data)
        return "delete reports"

    def update_mission(self, data: dict):
        """
        Удаляет сотрудника по его ID.
        :param employee_id: Идентификатор сотрудника.
        :return: Результат удаления.
        """
        try:
            mission = Mission.from_json_for_update("Mission", data=data)
        except Exception as e:
            return None

        res = self.db_engine.update(mission)
        return res


