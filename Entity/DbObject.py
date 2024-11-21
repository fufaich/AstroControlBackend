from abc import abstractmethod


class DbObject:
    def __init__(self, id: int, table_name:str):
        self._id = id
        self._table_name = table_name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def table_name(self):
        return self._table_name

    @table_name.setter
    def table_name(self, value: str):
        self._table_name = value

    def get_attributes(self) -> (list[str], list[any]):
        attributes = vars(self)
        public_attributes = {attr: value for attr, value in attributes.items() if not attr.startswith('_')}
        attribute_names = list(public_attributes.keys())
        attribute_values = list(public_attributes.values())

        return attribute_names, attribute_values

    def get_dict_attributes(self) -> dict[str, any]:
        return vars(self)