from datetime import datetime

from Entity.DbObject import DbObject
from utils.utils import parse_datetime


class Employee(DbObject):
    def __init__(self, id:int, table_name:str, surname:str, name:str, middle_name:str, post: str, specialization:str, date_of_birth:datetime, status_employee:str):
        super().__init__(id=id, table_name=table_name)
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.post = post
        self.specialization = specialization
        self.date_of_birth = date_of_birth
        self.status_employee = status_employee

    @classmethod
    def from_json(cls, table_name:str ,data: dict[str, str| int]):
        if 'id' not in data:
            data['id'] = None

        datetime_of_birth = parse_datetime(data['date_of_birth'])
        if datetime_of_birth is None:
            return None

        return cls(data['id'], table_name, data['surname'], data['name'], data['middle_name'], data['post'], data['specialization'], datetime_of_birth, data['status_employee'])

    @classmethod
    def clean(cls):
        return cls(None,None,None,None,None,None,None,None,None)


    @classmethod
    def from_json_for_update(cls, table_name:str ,data: dict[str, str]):
        if 'id' not in data:
            data['id'] = None
        tmp = Employee.clean()
        tmp.table_name = table_name
        for key in data.keys():
            if hasattr(tmp, key):
                setattr(tmp, key, data[key])

        return tmp

