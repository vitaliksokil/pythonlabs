import re


def palindrome(string):
    string = string.replace(' ', '')
    string = string.lower()
    string = re.sub(r"[.,;:!?'-]", '', string)
    reversed_string = string[::-1]
    if reversed_string == string:
        return True
    else:
        return False


string = input('Enter string: ')
print(palindrome(string))
