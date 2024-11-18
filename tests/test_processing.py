import pytest
from typing import Any
from src.processing import filter_by_state


def test_assert_filter_by_state():
    assert filter_by_state([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
    assert filter_by_state([{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}], user_state="CANCELED" ) == [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}]
    assert filter_by_state() == 'Данные с указанным статусом отсутсвуют'
    assert filter_by_state(()) == 'Неверный тип данных'
    assert filter_by_state({}) == 'Неверный тип данных'
    assert filter_by_state([]) == 'Данные с указанным статусом отсутсвуют'

