from datetime import datetime

from Entity.DbObject import DbObject


class ReportsJournal(DbObject):
    def __init__(self, id:int, table_name: str, header:str, content: str, data: datetime, id_employee: int):
        super().__init__(id=id, table_name=table_name)
        self.header = header
        self.content = content
        self.data = data
        self.id_employee = id_employee


    @classmethod
    def from_json(cls, table_name:str ,data: dict[str, str| int]):
        if 'id' not in data:
            data['id'] = None

        data = parse_datetime(data['data'])
        if data is None:
            return None


        return cls(data['id'], table_name, data['header'], data['content'], data, data['id_employee'])

    @classmethod
    def clean(cls):
        return cls(None,None,None,None,None,None, None, None)


    @classmethod
    def from_json_for_update(cls, table_name:str ,data: dict[str, str]):
        if 'id' not in data:
            data['id'] = None
        tmp = ReportsJournal.clean()
        tmp.table_name = table_name
        for key in data.keys():
            if hasattr(tmp, key):
                setattr(tmp, key, data[key])
        return tmp

