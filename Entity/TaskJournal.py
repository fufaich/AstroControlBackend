from datetime import datetime

from Entity.DbObject import DbObject


class TaskJournal(DbObject):
    def __init__(self, id:int, table_name: str, description: str, deadline: datetime, status:str, id_experiment: int, priority: int):
        super().__init__(id=id, table_name=table_name)
        self.description = description
        self.deadline = deadline
        self.status = status
        self.id_experiment = id_experiment
        self.priority = priority



    @classmethod
    def from_json(cls, table_name:str ,data: dict[str, str| int]):
        if 'id' not in data:
            data['id'] = None

        deadline = parse_datetime(data['deadline'])
        if deadline is None:
            return None


        return cls(data['id'], table_name, data['description'], deadline, data['status'], data['id_experiment'], data['priority'])

    @classmethod
    def clean(cls):
        return cls(None,None,None,None,None,None, None, None)


    @classmethod
    def from_json_for_update(cls, table_name:str ,data: dict[str, str]):
        if 'id' not in data:
            data['id'] = None
        tmp = TaskJournal.clean()
        tmp.table_name = table_name
        for key in data.keys():
            if hasattr(tmp, key):
                setattr(tmp, key, data[key])
        return tmp

