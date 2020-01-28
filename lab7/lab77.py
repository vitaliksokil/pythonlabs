import re


def case_change(string):
    if re.findall(r'[a-z]+_[a-z]+',string,re.MULTILINE):
        to_camel = lambda reg: reg.group(2).upper()
        matches_snake = re.sub(r'(_)([a-z])', to_camel, string)
        return matches_snake
    else:
        to_snake = lambda reg: reg.group(1).lower() + '_' + reg.group(2).lower()
        matches_camel = re.sub(r'([a-z]+)+([A-Z])', to_snake, string)
        return matches_camel


string = input('Enter string: ')
print(case_change(string))
