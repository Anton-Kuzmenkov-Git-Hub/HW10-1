from logging import raiseExceptions

import pytest
import datetime

from src.widgetv2 import mask_account_card, acceptable_names, acceptable_card_names, get_date
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('value, expected',[
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Счет 35383033474447895560', 'Счет **5560'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
    ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
    ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
    ('Счет 73654108430135874305', 'Счет **4305'),
])
def test_mark_param_mask_account_card(value, expected):
    assert mask_account_card(value) == expected

def test_assert_mask_account_card():
    assert mask_account_card() == ' Ошибка ввода данных'
    assert mask_account_card('0123')
    assert mask_account_card('Счет 0123')
    assert mask_account_card('Счет 01234567123456780123') == "Счет **0123"
    assert mask_account_card('Visa Gold 8990922113665229') == "Visa Gold 8990 92** **** 5229"



@pytest.mark.parametrize('time_moment, result',[
    ('1961-06-23T23:59:59.456789', '23.06.1961'),
    ('1968-03-22T23:59:59.456789', '22.03.1968'),
    ('1993-11-04T23:59:59.456789', '04.11.1993'),
    ('1998-06-13T23:59:59.456789', '13.06.1998'),
])
def test_mark_get_date(time_moment, result):
    assert get_date(time_moment) == result

def test_assert_get_date():
    assert get_date() == 'Отсутствуют данные о времени транзакции'
    assert get_date('12345abcde') == 'Неверный формат даты'
    assert get_date('2024-12-30T23:59:59.456789') == '30.12.2024'

