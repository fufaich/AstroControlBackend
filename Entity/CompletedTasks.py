from datetime import datetime

from Entity.DbObject import DbObject


class CompletedTasks(DbObject):
    def __init__(self, id:int, table_name: str,id_recource: int, id_report: int, id_task:int, id_employee: int):
        super().__init__(id=id, table_name=table_name)
        self.id_recource = id_recource
        self.id_report = id_report
        self.id_task = id_task
        self.id_employee = id_employee

    @classmethod
    def from_json(cls, table_name:str ,data: dict[str, str| int]):
        if 'id' not in data:
            data['id'] = None


        return cls(data['id'], table_name, data['id_recource'], data['id_report'], data['id_task'], data['id_employee'])

    @classmethod
    def clean(cls):
        return cls(None,None,None,None,None,None)


    @classmethod
    def from_json_for_update(cls, table_name:str ,data: dict[str, str]):
        if 'id' not in data:
            data['id'] = None
        tmp = CompletedTasks.clean()
        tmp.table_name = table_name
        for key in data.keys():
            if hasattr(tmp, key):
                setattr(tmp, key, data[key])
        return tmp

