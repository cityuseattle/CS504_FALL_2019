def is_phone_number(text):
    if len(text) != 12:
        return False

    for i in range(3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True

phone_number = '123-456-7890'
print('Is this phone number in a correct format?')
print(is_phone_number(phone_number))
