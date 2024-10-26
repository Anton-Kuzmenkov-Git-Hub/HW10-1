from os.path import split

import masks

operation_data = "2024-03-11T02:26:18.671407"
type_and_number = "Visa Classic 6831982476737658"



def mask_account_card (type_and_number: str) -> str:
    list_with_data = type_and_number.split()
    text_with_data = []
    for word_or_number in list_with_data:
        if word_or_number.isalpha():
            text_with_data.append(word_or_number)
        if word_or_number.isdigit():
            if len(word_or_number) <= 16:
                add_mask_to_card = f"{word_or_number[:4]} {word_or_number[4:6]}** **** {word_or_number[12:]}"
                text_with_data.append(add_mask_to_card)
            if len(word_or_number) > 16:
                add_mask_to_account = f"**{word_or_number[16:]}"
                text_with_data.append(add_mask_to_account)
    all_data = " ".join(text_with_data)
    return all_data


#def get_date(operation_data: str) -> str:
#    """Функция, которая преобразует входные данные о дате транзакции"""
#    return f"{operation_data[8:10]}.{operation_data[5:7]}.{operation_data[0:4]}"


#print (get_date(operation_data))
print (mask_account_card(type_and_number))