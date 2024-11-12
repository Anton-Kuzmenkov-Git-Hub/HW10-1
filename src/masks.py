#card_number = '7000792289606361'
#card_number = 'abcde792289406361'
# account_number = "73654108430135874305"
from itertools import count


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    card_num = str(card_number)
    count_digits = 0
    clean_digits = []
    for sign in card_num:
        if sign.isdigit():
            count_digits += 1
            clean_digits.append(sign)
    if count_digits != 16:
        return 'Введите правильно 16-ти значный номер карты'
    result_digits = "".join(clean_digits)
    if count_digits == 16:
        return f"{result_digits[:4]} {result_digits[4:6]}** **** {result_digits[12:]}"



print(get_mask_card_number('12341 2341 23 41234'))


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""

    return f"**{account_number[16:]}"


# print(get_mask_account(account_number))
