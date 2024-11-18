from datetime import date
import datetime

from src.masks import get_mask_account, get_mask_card_number


acceptable_names = ['Maestro', 'MasterCard', 'Visa Classic',
                    'Visa Platinum', 'Visa Gold', 'Счет']
acceptable_card_names = ['Maestro', 'MasterCard', 'Visa Classic',
                    'Visa Platinum', 'Visa Gold']

class MyClassError(Exception):
    pass

def mask_account_card(type_and_number: str = 'Card_or_account 0000000000000000') -> str:
    """Функция, которая возвращает строку с названием карты
    или счет и маскирует номер карты или счета"""
    list_with_data = type_and_number.split()
    if len(list_with_data) == 3:
        list_with_data = [f'{list_with_data[0]} {list_with_data[1]}', list_with_data[-1]]
    try:
        text_with_alpha = []
        if list_with_data[0] in acceptable_names:
            text_with_alpha.append(list_with_data[0])
        text_with_digit = []
        for num in list_with_data:
            if num.isdigit():
                if len(num) == 16:
                    add_mask_to_card = get_mask_card_number(num)
                    text_with_digit.append(add_mask_to_card)
                if len(num) == 20:
                    add_mask_to_account = get_mask_account(num)
                    text_with_digit.append(add_mask_to_account)
                if len(num) != 16 and len(num) != 20:
                    add_mask_to_account = 'Не удается определить номер карты или счета'
                    text_with_digit.append(add_mask_to_account)
                    raise MyClassError('Некорректный ввод номера карты или счета')
        all_data = " ".join(text_with_alpha) + ' ' + " ".join(text_with_digit)
        if 'Несуществующая карта или счет' in all_data:
            return 'Некорректный ввод названия карты или счета'
        if 'Счет' in text_with_alpha and len(text_with_digit[0]) == 6:
            return all_data
        if set(text_with_alpha).issubset(acceptable_card_names) and len(text_with_digit[0]) == 19:
            return all_data
        else:
            return 'Проверьте правильность ввода данных'
    except MyClassError as mce:
        return mce


#print (mask_account_card())




def get_date(operation_data: str = '1000-12-30T23:59:59.456789') -> date:
    """Функция, которая преобразует входные данные о дате транзакции"""
    try:
        date_time_obj = datetime.datetime.strptime(operation_data, '%Y-%m-%dT%H:%M:%S.%f')
        if operation_data == "1000-12-30T23:59:59.456789":
            return "Отсутствуют данные о времени транзакции"
        else:
            return date_time_obj.strftime('%d.%m.%Y')
    except ValueError:
        return 'Неверный формат даты'


print (get_date('2024-12-30T23:59:59.456789'))

