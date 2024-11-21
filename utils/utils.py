from datetime import datetime


def parse_datetime(date_str: str) -> datetime|None:
    """
    Преобразует строку с датой в формате 2003-08-16 в объект datetime.

    :param date_str: Строка с датой.
    :return: Объект datetime.
    """
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print(f"Ошибка парсинга: неверный формат даты '{date_str}'. Ожидается формат 'YYYY-MM-DD'.")
        return None


def get_str_attributes(list_attributes):
    return ', '.join(list_attributes)

def get_str_values(list_values):
    list_values = [str(i.date()) if isinstance(i, datetime) else str(i) for i in list_values]
    str_values = ", ".join([f"'{item}'" for item in list_values])
    return str_values

def clean_dict(dictionary: dict[str, any]) -> dict[str, any]:
    result = {}
    for key, value in dictionary.items():
        if value is not None and not key.startswith('_'):
            result[key] = value

    return result