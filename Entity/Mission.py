from datetime import datetime

from Entity.DbObject import DbObject

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

class Mission(DbObject):
    def __init__(self, id:int, table_name: str, name:str, start_mission: datetime, end_mission: datetime, description:str, status_mission: str, id_employee:int):
        super().__init__(id=id, table_name=table_name)
        self.name = name
        self.description = description
        self.start_mission = start_mission
        self.end_mission = end_mission
        self.status_mission = status_mission
        self.id_employee = id_employee


    @classmethod
    def from_json(cls, table_name:str ,data: dict[str, str| int]):
        if 'id' not in data:
            data['id'] = None

        start_mission = parse_datetime(data['start_mission'])
        if start_mission is None:
            return None

        end_mission = parse_datetime(data['end_mission'])
        if end_mission is None:
            return None

        return cls(data['id'], table_name, data['name'], start_mission, end_mission, data['description'], data['status_mission'], data['id_employee'])

    @classmethod
    def clean(cls):
        return cls(None,None,None,None,None,None, None, None)


    @classmethod
    def from_json_for_update(cls, table_name:str ,data: dict[str, str]):
        if 'id' not in data:
            data['id'] = None
        tmp = Mission.clean()
        tmp.table_name = table_name
        for key in data.keys():
            if hasattr(tmp, key):
                setattr(tmp, key, data[key])
        return tmp

