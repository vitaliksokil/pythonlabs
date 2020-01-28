import re


def is_sequence_brackets_correct(string):
    matches = re.findall(r"[(){}\[\]<>]", string, re.MULTILINE)
    stack = []
    for match in matches:
        if re.match(r"[)}\]>]", match):
            if not stack:
                return False
            stackpop = stack.pop()
            if re.match(r"[({\[<]", stackpop):
                temp = stackpop + match
                if re.match(r"(\(\)|\{\}|\[\]|\<\>)", temp):
                    continue
                else:
                    return False
        else:
            stack.append(match)

    return bool(not stack)


string = input('Enter string: ')
print(is_sequence_brackets_correct(string))
