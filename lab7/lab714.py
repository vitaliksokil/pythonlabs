import re


def is_correct_email(string):
    if re.match(r'[A-Za-z0-9]+@[A-Za-z]+.[a-z]{2,}', string, re.IGNORECASE):
        return True
    else:
        return False


string = input('Enter email: ')
print(is_correct_email(string))
