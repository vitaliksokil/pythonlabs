import re


def number_of_vowels(string):
    matches = re.findall(r'[aouiey]', string, re.IGNORECASE)
    return len(matches)


string = input('Enter string: ')
print(number_of_vowels(string))
