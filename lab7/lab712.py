import re


def delete_extra_spaces(string):
    string = re.sub(r'\s{2,}', ' ', string)
    return string


string = input('Enter string: ')
print(delete_extra_spaces(string))
