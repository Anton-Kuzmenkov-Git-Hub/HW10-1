from masks import get_mask_account, get_mask_card_number
import datetime

acceptable_names = ['Maestro', 'MasterCard', 'Visa Classic',
                    'Visa Platinum', 'Visa Gold', 'Счет']
acceptable_card_names = ['Maestro', 'MasterCard', 'Visa Classic',
                    'Visa Platinum', 'Visa Gold']


def mask_account_card(type_and_number = 'card_or_account_and_number') -> str:
    """Функция, которая возвращает строку с названием карты
    или счет и маскирует номер карты или счета"""
    list_with_data = type_and_number.split()
    text_with_alpha = []
    for word_or_number in list_with_data:
        if word_or_number.isalpha():
            if word_or_number in acceptable_names:
                text_with_alpha.append(word_or_number)
            if word_or_number not in acceptable_names:
                add_text = 'Несуществующая карта или счет'
                text_with_alpha.append(add_text)
    text_with_digit = []
    for word_or_number in list_with_data:
        if word_or_number.isdigit():
            if len(word_or_number) == 16:
                add_mask_to_card = get_mask_card_number(word_or_number)
                text_with_digit.append(add_mask_to_card)
            if len(word_or_number) == 20:
                add_mask_to_account = get_mask_account(word_or_number)
                text_with_digit.append(add_mask_to_account)
            if len(word_or_number) != 16 and len(word_or_number) != 20:
                add_mask_to_account = 'Не удается определить номер карты или счета'
                text_with_digit.append(add_mask_to_account)
    all_data = " ".join(text_with_alpha) + ' ' + " ".join(text_with_digit)
    if 'Не удается определить номер карты или счета' in all_data:
        return 'Некорректный ввод номера карты или счета'
    if 'Несуществующая карта или счет' in all_data:
        return 'Некорректный ввод названия карты или счета'
    if 'Счет' in text_with_alpha and len(text_with_digit[0]) == 6:
        return all_data
    if set(text_with_alpha).issubset(acceptable_card_names) and len(text_with_digit[0]) == 19:
        return all_data
    else:
        return 'Проверьте правильность ввода данных'


print (mask_account_card('1111222233334444 Maestro'))





def get_date(operation_data: str) -> str:
    """Функция, которая преобразует входные данные о дате транзакции"""
    dt_str = operation_data
    dt = datetime.datetime.fromisoformat(dt_str)
    return dt

#print (get_date("2024-03-11T02:26:18.671407"))