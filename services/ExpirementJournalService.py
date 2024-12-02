from Entity.ExperimentJournal import ExperimentJournal
from database.DatabaseEngine import DatabaseEngine
from database.DatabaseConfig import DatabaseConfig

class ExperimentJournalService:
    def __init__(self):
        # Инициализация соединения с базой данных через DatabaseEngine
        self.db_engine = DatabaseEngine(DatabaseConfig.get_config())

    def get_experiment(self, filters: dict):
        """
        Получает список сотрудников с фильтрацией.
        :param filters: Словарь с фильтрами (например, {"role": "manager"}).
        :return: Список сотрудников.
        """
        experiment = self.db_engine.get("ExperimentJournal", filters=filters)
        return experiment

    def add_experiment(self, data: dict) -> str:
        """
        Добавляет ново.
        :param data: Словарь с данными сотрудника (например, {"name": "John", "role": "manager"}).
        :return: Результат добавления.
        """
        try:
            experiment = ExperimentJournal.from_json("ExperimentJournal", data=data)
        except Exception as e:
            return f"Add failed: {e}"

        return self.db_engine.add(experiment)

    def delete_experiment(self, data: dict):
        """
        Удаляет сотрудника по его ID.
        :param data:
        :param employee_id: Идентификатор сотрудника.
        :return: Результат удаления.
        """
        self.db_engine.delete("ExperimentJournal", data)
        return "delete experiment"

    def update_experiment(self, data: dict):
        """
        Удаляет сотрудника по его ID.
        :param employee_id: Идентификатор сотрудника.
        :return: Результат удаления.
        """
        try:
            experiment = ExperimentJournal.from_json_for_update("ExperimentJournal", data=data)
        except Exception as e:
            return None

        res = self.db_engine.update(experiment)
        return res


