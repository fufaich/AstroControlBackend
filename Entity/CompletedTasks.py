from database.DbObject import DbObject


class CompletedTasks(DbObject):
    def __init__(self, table_name: str, id_resource: int, id_report: int, id_task:int, id_employee: int):
        super().__init__(table_name=table_name)
        self.id_resource = id_resource
        self.id_report = id_report
        self.id_task = id_task
        self.id_employee = id_employee

    @classmethod
    def from_json(cls, table_name:str ,data: dict[str, str| int]):
        return cls(table_name, data['id_resource'], data['id_report'], data['id_task'], data['id_employee'])

    @classmethod
    def clean(cls):
        return cls("CompletedTasks",None,None,None,None)


    @classmethod
    def from_json_for_update(cls, table_name:str ,data: dict[str, str]):
        tmp = CompletedTasks.clean()
        tmp.table_name = table_name
        for key in data.keys():
            if hasattr(tmp, key):
                setattr(tmp, key, data[key])
        return tmp

