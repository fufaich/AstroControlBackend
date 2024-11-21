from datetime import datetime

from Entity.DbObject import DbObject


class Resources(DbObject):
    def __init__(self, id:int, table_name: str, name:str, count: int, unit: str):
        super().__init__(id=id, table_name=table_name)
        self.name = name
        self.count = count
        self.unit = unit


    @classmethod
    def from_json(cls, table_name:str ,data: dict[str, str| int]):
        if 'id' not in data:
            data['id'] = None

        return cls(data['id'], table_name, data['name'], data['count'], data['unit'])

    @classmethod
    def clean(cls):
        return cls(None,None,None,None,None)


    @classmethod
    def from_json_for_update(cls, table_name:str ,data: dict[str, str]):
        if 'id' not in data:
            data['id'] = None
        tmp = Resources.clean()
        tmp.table_name = table_name
        for key in data.keys():
            if hasattr(tmp, key):
                setattr(tmp, key, data[key])
        return tmp

