import pytest
from typing import Any
from src.processing import filter_by_state


@pytest.mark.parametrize('value, expected',[
    ([{"id": 12345678, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}], [{"id": 12345678, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]),
    ([{"id": 12345678, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"}], 'Данные с указанным статусом отсутсвуют'),
    ({"id": 12345678, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"}, 'Неверный тип данных'),
    ([{"id": 12345678, "state": "OTHER", "date": "2019-07-03T18:35:29.512364"}], 'Данные с указанным статусом отсутсвуют'),
])

def test_mark_param_filter_by_state(value, expected):
    assert filter_by_state(value) == expected


def test_assert_filter_by_state(short_data_other, short_data_canceled):
    assert filter_by_state(short_data_other) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
    assert filter_by_state(short_data_other,user_state="OTHER") == 'Данные с указанным статусом отсутсвуют'
    assert filter_by_state(short_data_canceled, user_state="CANCELED" ) == [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}]
    assert filter_by_state() == 'Данные с указанным статусом отсутсвуют'
    assert filter_by_state(()) == 'Неверный тип данных'
    assert filter_by_state({}) == 'Неверный тип данных'
    assert filter_by_state([]) == 'Данные с указанным статусом отсутсвуют'
    assert filter_by_state(12345) == 'Неверный тип данных'
    assert filter_by_state([], user_state='CANCELED') == 'Данные с указанным статусом отсутсвуют'
    assert filter_by_state([], user_state=None) == 'Данные с указанным статусом отсутсвуют'