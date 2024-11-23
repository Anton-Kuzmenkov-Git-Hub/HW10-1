import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize('value, expected', [
    ([{"id": 12345678, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
     [{"id": 12345678, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]),
    ([{"id": 12345678, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"}],
     'Данные с указанным статусом отсутсвуют'),
    ({"id": 12345678, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
     'Неверный тип данных'),
    ([{"id": 12345678, "state": "OTHER", "date": "2019-07-03T18:35:29.512364"}],
     'Данные с указанным статусом отсутсвуют'),
])
def test_mark_param_filter_by_state(value, expected):
    assert filter_by_state(value) == expected


def test_assert_filter_by_state(short_data_other, short_data_canceled):
    assert filter_by_state(short_data_other) == [{'id': 41428829, 'state': 'EXECUTED',
                                                  'date': '2019-07-03T18:35:29.512364'}]
    assert filter_by_state(short_data_other, user_state="OTHER") == 'Данные с указанным статусом отсутсвуют'
    assert filter_by_state(short_data_canceled, user_state="CANCELED") == [{"id": 594226727, "state": "CANCELED",
                                                                            "date": "2018-09-12T21:27:25.241689"}]
    assert filter_by_state() == 'Данные с указанным статусом отсутсвуют'
    assert filter_by_state(()) == 'Неверный тип данных'
    assert filter_by_state({}) == 'Неверный тип данных'
    assert filter_by_state([]) == 'Данные с указанным статусом отсутсвуют'
    assert filter_by_state(int) == 'Неверный тип данных'
    assert filter_by_state([], user_state='CANCELED') == 'Данные с указанным статусом отсутсвуют'
    assert filter_by_state([], user_state=None) == 'Данные с указанным статусом отсутсвуют'


def test_assert_sort_by_date(example_data, answer, answer_rev_falls, same_data, same_data_answer, data_error):
    assert sort_by_date(example_data) == answer
    assert sort_by_date(example_dict=example_data, order=True) == answer
    assert sort_by_date(example_dict=example_data, order=False) == answer_rev_falls
    assert sort_by_date(example_dict=example_data, order=None) == 'Задайте порядок сортировки'
    assert sort_by_date(example_dict=example_data, order='None') == 'Задайте порядок сортировки'
    assert sort_by_date(example_dict=example_data, order=12345) == 'Задайте порядок сортировки'
    assert sort_by_date(example_dict=same_data) == same_data_answer
    assert sort_by_date(data_error) == 'Неверный формат даты'
    assert sort_by_date(example_dict=data_error, order=False) == 'Неверный формат даты'
    assert sort_by_date([]) == ('Образец данных [{"id": 41428829, "state": "EXECUTED", '
                                '"date": "2019-07-03T18:35:29.512364"}]')
    assert sort_by_date(()) == 'Неверный тип данных'
    assert sort_by_date({}) == 'Неверный тип данных'
    assert sort_by_date(str) == 'Неверный тип данных'
    assert sort_by_date(int) == 'Неверный тип данных'
    assert sort_by_date(float) == 'Неверный тип данных'
