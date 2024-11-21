from datetime import datetime

from Entity.CompletedTasks import CompletedTasks
from Entity.Employee import Employee
from Entity.ExperimentJournal import ExperimentJournal
from Entity.Mission import Mission
from Entity.ReportsJournal import ReportsJournal
from Entity.Resources import Resources
from Entity.TaskJournal import TaskJournal


def parse_datetime(date_str: str) -> datetime|None:
    """
    Преобразует строку с датой в формате 2003-08-16 в объект datetime.

    :param date_str: Строка с датой.
    :return: Объект datetime.
    """
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print(f"Ошибка парсинга: неверный формат даты '{date_str}'. Ожидается формат 'YYYY-MM-DD'.")
        return None


def get_str_attributes(list_attributes):
    return ', '.join(list_attributes)

def get_str_values(list_values):
    list_values = [str(i.date()) if isinstance(i, datetime) else str(i) for i in list_values]
    str_values = ", ".join([f"'{item}'" for item in list_values])
    return str_values

def clean_dict(dictionary: dict[str, any]) -> dict[str, any]:
    result = {}
    for key, value in dictionary.items():
        if value is not None and not key.startswith('_'):
            result[key] = value

    return result

def create_db_object(table_name:str, data:dict[str, any]):
    match table_name:
        case "Employee":
            return Employee.from_json(table_name=table_name ,data=data)
        case "CompletedTasks":
            return CompletedTasks.from_json(table_name=table_name ,data=data)
        case "ExperimentJournal":
            return ExperimentJournal.from_json(table_name=table_name ,data=data)
        case "Mission":
            return Mission.from_json(table_name=table_name, data=data)
        case "ReportsJournal":
            return ReportsJournal.from_json(table_name=table_name, data=data)
        case "Resources":
            return Resources.from_json(table_name=table_name, data=data)
        case "TaskJournal":
            return TaskJournal.from_json(table_name=table_name, data=data)
        case "_":
            return None

def create_db_object_for_update(table_name:str, data:dict[str, any]):
    match table_name:
        case "Employee":
            return Employee.from_json_for_update(table_name=table_name ,data=data)
        case "CompletedTasks":
            return CompletedTasks.from_json_for_update(table_name=table_name ,data=data)
        case "ExperimentJournal":
            return ExperimentJournal.from_json_for_update(table_name=table_name ,data=data)
        case "Mission":
            return Mission.from_json_for_update(table_name=table_name, data=data)
        case "ReportsJournal":
            return ReportsJournal.from_json_for_update(table_name=table_name, data=data)
        case "Resources":
            return Resources.from_json_for_update(table_name=table_name, data=data)
        case "TaskJournal":
            return TaskJournal.from_json_for_update(table_name=table_name, data=data)
        case "_":
            return None