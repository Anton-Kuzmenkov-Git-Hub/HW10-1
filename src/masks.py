from itertools import count



def get_mask_card_number(card_number: str = '0000000000000000') -> str:
    """Функция, которая маскирует номер карты"""
    card_num = str(card_number)
    count_digits = 0
    clean_digits = []
    for sign in card_num:
        if sign.isdigit():
            count_digits += 1
            clean_digits.append(sign)
    if count_digits != 16:
        return "Введите правильно 16-ти значный номер карты"
    result_digits = "".join(clean_digits)
    if count_digits == 16:
        if result_digits == '0000000000000000':
            return 'Ошибка ввода данных'
        else:
            return f"{result_digits[:4]} {result_digits[4:6]}** **** {result_digits[12:]}"



# print(get_mask_card_number())


def get_mask_account(account_number: str ='00000000000000000000') -> str:
    """Функция, которая маскирует номер счета"""
    if isinstance(account_number, str):
        count_digits = 0
        clean_digits = []
        for sign in account_number:
            if sign.isdigit():
                count_digits += 1
                clean_digits.append(sign)
        if count_digits != 20:
            return "Введите правильно 20-ти значный номер счета"
        result_digits = "".join(clean_digits)
        if count_digits == 20:
            if result_digits == '00000000000000000000':
                return 'Ошибка ввода данных'
            else:
                return f"**{result_digits[16:]}"
    return "Неверный формат ввода"


# print(get_mask_account('1111 4444 2222 5555 3333'))
