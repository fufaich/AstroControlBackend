

class DbObject:
    def __init__(self, table_name:str):
        self._table_name = table_name

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