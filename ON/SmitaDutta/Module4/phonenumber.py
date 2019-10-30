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

    return True



phoneNumber = '206-555-5555'
print("Is it a phone number with the right format?")
print(is_phone_number(phoneNumber))