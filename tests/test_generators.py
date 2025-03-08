import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions


# 1) Напишите тесты, проверяющие, что функция корректно фильтрует транзакции по заданной валюте.
# 2) Проверьте, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют.
# 3) Убедитесь, что генератор не завершается ошибкой при обработке пустого списка
# или списка без соответствующих валютных операций.


def test_assert_filter_by_currency(usd_1, usd_2, usd_3, rub_1, rub_2):
    i_usd = filter_by_currency(transactions, 'USD')
    i_rub = filter_by_currency(transactions, 'RUB')
    assert next(i_usd) == usd_1
    assert next(i_usd) == usd_2
    assert next(i_usd) == usd_3
    assert next(i_rub) == rub_1
    assert next(i_rub) == rub_2


def test_wd():
    with pytest.raises(TypeError, match='Выберите в качестве валюты USD или RUB.'):
        list(filter_by_currency(transactions, 'EUR'))


def test_transaction_descriptions():
    descr = transaction_descriptions (transactions)
    assert next(descr) == 'Перевод организации'
    assert next(descr) == 'Перевод со счета на счет'
    assert next(descr) == 'Перевод со счета на счет'
    assert next(descr) == 'Перевод с карты на карту'
    assert next(descr) == 'Перевод организации'
    assert next(descr) == '???'

