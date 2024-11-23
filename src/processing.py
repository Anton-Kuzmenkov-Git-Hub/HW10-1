import datetime
from typing import Any

example = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

example_2 = [
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-10-14T21:27:25.241689'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-10-14T02:08:58.425572'},
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2018-10-14T18:35:29.512364'},
]


def filter_by_state(example_dict: list[dict[str, Any]] = [],
                    user_state: str = "EXECUTED") -> str | list[dict[str, Any]]:
    """Функция, которая возвращает новый список словарей, в соответсвии с заданным параметром state"""
    if isinstance(example_dict, list):
        new_dictionary = []
        for i in example_dict:
            if i["state"] == user_state:
                new_dictionary.append(i)
        if not new_dictionary:
            return 'Данные с указанным статусом отсутсвуют'
        return new_dictionary
    return 'Неверный тип данных'
# print(filter_by_state(example))


def sort_by_date(example_dict=None, order: bool = True) -> list[dict[str, Any]] | str:
    """Функция, которая возвращает новый список отсортированный по дате"""
    if example_dict is None:
        example_dict = []
    try:
        if isinstance(example_dict, list):
            if not example_dict:
                return 'Образец данных [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]'
            new_dict = []
            if example_dict:
                if order is not True and order is not False:
                    return 'Задайте порядок сортировки'
                for i in example_dict:
                    evry_data = (i['date'])
                    slice_data = evry_data[8:10] + '.' + evry_data[5:7] + '.' + evry_data[0:4]
                    convert_data = (datetime.datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S.%f'))
                    slice_convert_data = convert_data.strftime('%d.%m.%Y')
                    if slice_data == slice_convert_data:
                        new_dict.append(i)
            sort_new_dict = sorted(new_dict, key=lambda x: x["date"], reverse=order)
            return sort_new_dict
        return 'Неверный тип данных'
    except ValueError:
        return 'Неверный формат даты'

# print(sort_by_date(example, order=False))
