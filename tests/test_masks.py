import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('value, expected', [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1111222233334444", "1111 22** **** 4444"),
    ("0123456789012345", "0123 45** **** 2345"),
])
def test_mark_get_mask_card_number(value, expected):
     assert get_mask_card_number(value) == expected

def test_assert_get_mask_card_number():
    assert get_mask_card_number("1234") == 'Введите правильно 16-ти значный номер карты'
    assert get_mask_card_number(1234) == 'Введите правильно 16-ти значный номер карты'
    assert get_mask_card_number(0) == 'Введите правильно 16-ти значный номер карты'
    assert get_mask_card_number("0123 4567 8910 1112 1314") == 'Введите правильно 16-ти значный номер карты'
    assert get_mask_card_number("abcd") == 'Введите правильно 16-ти значный номер карты'
    assert get_mask_card_number("1234") == 'Введите правильно 16-ти значный номер карты'
    assert get_mask_card_number(7000792289606361) == '7000 79** **** 6361'
    assert get_mask_card_number('0123 45 678 9101112') == '0123 45** **** 1112'
    assert get_mask_card_number('0123 ab cd 9101112') == 'Введите правильно 16-ти значный номер карты'
    assert get_mask_card_number() == 'Ошибка ввода данных'


def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'
    assert get_mask_account(73654108430135874305) == 'Неверный формат ввода'
    assert get_mask_account('1111aaaa2222bbbb3333') == 'Введите правильно 20-ти значный номер счета'
    assert get_mask_account('1234') == 'Введите правильно 20-ти значный номер счета'
    assert get_mask_account('1111222233334444555566667777') == 'Введите правильно 20-ти значный номер счета'
    assert get_mask_account('adcd') == 'Введите правильно 20-ти значный номер счета'
    assert get_mask_account('1111 2222 3333 4444 5555') == '**5555'
    assert get_mask_account() == 'Ошибка ввода данных'
