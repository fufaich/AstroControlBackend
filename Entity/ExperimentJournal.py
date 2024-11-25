from datetime import datetime

from database.DbObject import DbObject



class ExperimentJournal(DbObject):
    def __init__(self, id:int, table_name: str, name: str, description: str, start_experiment: datetime, end_experiment: datetime, status: str, id_employee: int, id_mission: int):
        super().__init__(id=id, table_name=table_name)
        self.name = name
        self.description = description
        self.start = start_experiment
        self.end = end_experiment
        self.status = status
        self.id_employee = id_employee
        self.id_mission = id_mission


    @classmethod
    def from_json(cls, table_name:str ,data: dict[str, str| int]):
        if 'id' not in data:
            data['id'] = None

        start_experiment = parse_datetime(data['start'])
        if start_experiment is None:
            return None

        end_experiment = parse_datetime(data['end'])
        if end_experiment is None:
            return None

        return cls(data['id'], table_name, data['name'], data['description'], start_experiment, end_experiment, data['status'], data['id_employee'], data['id_mission'])

    @classmethod
    def clean(cls):
        return cls(None,None,None,None,None,None, None, None, None)


    @classmethod
    def from_json_for_update(cls, table_name:str ,data: dict[str, str]):
        if 'id' not in data:
            data['id'] = None
        tmp = ExperimentJournal.clean()
        tmp.table_name = table_name
        for key in data.keys():
            if hasattr(tmp, key):
                setattr(tmp, key, data[key])
        return tmp

