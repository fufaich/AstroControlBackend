from Entity.ReportsJournal import ReportsJournal
from database.DatabaseEngine import DatabaseEngine
from database.DatabaseConfig import DatabaseConfig

class ReportsJournalService:
    def __init__(self):
        # Инициализация соединения с базой данных через DatabaseEngine
        self.db_engine = DatabaseEngine(DatabaseConfig.get_config())

    def get_reports(self, filters: dict):
        """
        Получает список сотрудников с фильтрацией.
        :param filters: Словарь с фильтрами (например, {"role": "manager"}).
        :return: Список сотрудников.
        """
        reports = self.db_engine.get("Resources", filters=filters)
        return reports

    def add_reports(self, data: dict) -> str:
        """
        Добавляет ново.
        :param data: Словарь с данными сотрудника (например, {"name": "John", "role": "manager"}).
        :return: Результат добавления.
        """
        try:
            reports = ReportsJournal.from_json("ReportsJournal", data=data)
        except Exception as e:
            return "Add failed"

        return self.db_engine.add(reports)

    def delete_reports(self, data: dict):
        """
        Удаляет сотрудника по его ID.
        :param data:
        :param employee_id: Идентификатор сотрудника.
        :return: Результат удаления.
        """
        self.db_engine.delete("ReportsJournal", data)
        return "delete reports"

    def update_reports(self, data: dict):
        """
        Удаляет сотрудника по его ID.
        :param employee_id: Идентификатор сотрудника.
        :return: Результат удаления.
        """
        try:
            reports = ReportsJournal.from_json_for_update("ReportsJournal", data=data)
        except Exception as e:
            return None

        res = self.db_engine.update(reports)
        return res


