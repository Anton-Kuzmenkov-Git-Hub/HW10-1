import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('value, expected', [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1111222233334444", "1111 22** **** 4444"),
    ("0123456789012345", "0123 45** **** 2345"),
])
def test_get_mask_card_number(value, expected):
     assert get_mask_card_number(value) == expected

def test_for_get_mask_card_number():
    assert get_mask_card_number("1234") == 'Введите правильно 16-ти значный номер карты'
    assert get_mask_card_number(1234) == 'Введите правильно 16-ти значный номер карты'
    assert get_mask_card_number(0) == 'Введите правильно 16-ти значный номер карты'
    assert get_mask_card_number("0123 4567 8910 1112 1314") == 'Введите правильно 16-ти значный номер карты'
    assert get_mask_card_number("abcd") == 'Введите правильно 16-ти значный номер карты'
    assert get_mask_card_number("1234") == 'Введите правильно 16-ти значный номер карты'
    assert get_mask_card_number(7000792289606361) == '7000 79** **** 6361'
    assert get_mask_card_number('0123 45 678 9101112') == '0123 45** **** 1112'
    assert get_mask_card_number('0123 ab cd 9101112') == 'Введите правильно 16-ти значный номер карты'

