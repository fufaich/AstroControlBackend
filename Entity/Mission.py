from datetime import datetime

from database.DbObject import DbObject
from utils.utils import parse_datetime


class Mission(DbObject):
    def __init__(self, id_mission:int, table_name: str, name:str, start_mission: datetime, end_mission: datetime, description:str, status_mission: str, id_employee:int):
        super().__init__(table_name=table_name)
        self.name = name
        self.description = description
        self.start_mission = start_mission
        self.end_mission = end_mission
        self.status_mission = status_mission
        self.id_employee = id_employee
        self.id_mission = id_mission


    @classmethod
    def from_json(cls, table_name:str ,data: dict[str, str| int]):
        start_mission = parse_datetime(data['start_mission'])
        if start_mission is None:
            return None

        end_mission = parse_datetime(data['end_mission'])
        if end_mission is None:
            return None

        return cls(data['id_mission'], table_name, data['name'], start_mission, end_mission, data['description'], data['status_mission'], data['id_employee'])

    @classmethod
    def clean(cls):
        return cls(None,None,None,None,None,None, None, None)


    @classmethod
    def from_json_for_update(cls, table_name:str ,data: dict[str, str]):
        tmp = Mission.clean()
        tmp.table_name = table_name
        for key in data.keys():
            if hasattr(tmp, key):
                setattr(tmp, key, data[key])
        return tmp

