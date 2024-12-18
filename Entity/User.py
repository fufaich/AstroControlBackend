from database.DbObject import DbObject


class User(DbObject):
    def __init__(self, table_name: str, id_user: int, username:str, pass_hash: str, role: str):
        super().__init__(table_name=table_name)
        self.id_user = id_user
        self.username = username
        self.pass_hash = pass_hash
        self.role = role

    @classmethod
    def from_json(cls, table_name:str ,data: dict[str, str| int]):
        return cls(table_name,data['id_user'], data['username'], data['pass_hash'], data['role'])

    @classmethod
    def clean(cls):
        return cls(None,None, None,None,None)


    @classmethod
    def from_json_for_update(cls, table_name:str ,data: dict[str, str]):
        tmp = User.clean()
        tmp.table_name = table_name
        for key in data.keys():
            if hasattr(tmp, key):
                setattr(tmp, key, data[key])
        return tmp

