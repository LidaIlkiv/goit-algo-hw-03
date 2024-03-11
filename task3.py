import re

# phone_number = '38 (050) 671-21-21'
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number:str):
    formatted_number = re.sub(r'[^0-9+]', '', phone_number)
    if not formatted_number.startswith('+'):
        if formatted_number.startswith('380'):
            formatted_number = '+' + formatted_number
        else:
            formatted_number = '+38' + formatted_number

    return(formatted_number)
    

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

