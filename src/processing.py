from typing import Any

example = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(
    example: list[dict[str, Any]], user_state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """Функция, которая возвращает новый список словарей, в соответсвии с заданным параметром state"""
    new_dictionary = []
    for i in example:
        if i["state"] == user_state:
            new_dictionary.append(i)
    return new_dictionary


# print(filter_by_state(example, user_state="EXECUTED"))


def sort_by_date(
    example: list[dict[str, Any]], order: bool = True
) -> list[dict[str, Any]]:
    """Функция, которая возвращает новый список отсортированный по дате"""
    example_sorted_by_date = sorted(example, key=lambda x: x["date"], reverse=order)
    return example_sorted_by_date


# print(sort_by_date(example, order=True))
