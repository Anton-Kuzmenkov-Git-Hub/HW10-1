from typing import Generator

transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

def filter_by_currency(transaction: list[dict[str, any]] = [], currency: str = '') -> Generator[str,None,None] or str:
    """Функция принимает на вход список словарей, представляющих транзакции,
    и возвращает итератор, который поочередно выдает транзакции по заданной валюте"""
    if isinstance(transaction, list) and isinstance(currency, str):
        if transaction == []:
            return 'Список транзакций пуст'
        if currency == '':
            return 'Впишите в currency валюту USD или RUB.'
        if currency != 'USD' and currency != 'RUB':
            return 'Выберите в качестве валюты USD или RUB.'
        for t in transaction:
            if t["operationAmount"]["currency"]["code"] == currency:
                yield t
    return 'Неверный формат данных'



# f = filter_by_currency(transactions,currency='RB')
# while True:
#     try:
#         a = next(f)
#         print(a)
#     except StopIteration:
#         print ('Больше нет данных по выбранной валюте')
#         break

# usd_transactions = filter_by_currency(transactions, 'USD')
# try:
#     for a in range(10):
#         print(next(usd_transactions))
# except StopIteration:
#     print('Больше нет данных по валюте USD.')
#
# rub_transactions = filter_by_currency(transactions, 'RUB')
# try:
#     for a in range(10):
#         print(next(rub_transactions))
# except StopIteration:
#     print('Больше нет данных по валюте RUB.')



def transaction_descriptions (transaction: list[dict[str, any]]) -> Generator[str,None,None]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for d in transaction:
        yield d["description"]

# descriptions = transaction_descriptions(transactions)
# try:
#     for i in range(10):
#         print(next(descriptions))
# except StopIteration:
#     print('Больше нет операция по картам или счетам.')




def card_number_generator(start: int, end:int) -> Generator[str,None,None]:
    """Функция, которая может сгенерировать номера карт в заданном диапазоне"""
    real_end = end + 1
    for num in range(start,real_end, +1):
        card_number_for_gen = str(num)
        while len(card_number_for_gen) < 16:
            card_number_for_gen = '0' + card_number_for_gen
        result_card_number = f'{card_number_for_gen[:4]} {card_number_for_gen[4:9]} {card_number_for_gen[9:13]} {card_number_for_gen[12:]}'
        yield result_card_number

# for card_number in card_number_generator(1,5):
#     print (card_number)
