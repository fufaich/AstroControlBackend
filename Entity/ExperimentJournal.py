from datetime import datetime

from database.DbObject import DbObject
from utils.utils import parse_datetime


class ExperimentJournal(DbObject):
    def __init__(self, id_experiment:int, table_name: str, name: str, description: str, start_experiment: datetime, end_experiment: datetime, status: str, id_employee: int, id_mission: int):
        super().__init__(table_name=table_name)
        self.name = name
        self.description = description
        self.start_experiment = start_experiment
        self.end_experiment = end_experiment
        self.status = status
        self.id_experiment = id_experiment
        self.id_employee = id_employee
        self.id_mission = id_mission


    @classmethod
    def from_json(cls, table_name:str ,data: dict[str, str| int]):
        start_experiment = parse_datetime(data['start_experiment'])
        if start_experiment is None:
            return None

        end_experiment = parse_datetime(data['end_experiment'])
        if end_experiment is None:
            return None

        return cls(data['id_experiment'], table_name, data['name'], data['description'], start_experiment, end_experiment, data['status'], data['id_employee'], data['id_mission'])

    @classmethod
    def clean(cls):
        return cls(None,None,None,None,None,None, None, None, None)


    @classmethod
    def from_json_for_update(cls, table_name:str ,data: dict[str, str]):
        tmp = ExperimentJournal.clean()
        tmp.table_name = table_name
        for key in data.keys():
            if hasattr(tmp, key):
                setattr(tmp, key, data[key])
        return tmp

