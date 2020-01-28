def border_string(string):
    string = string.strip()
    length = len(string)
    border_top_bot = ('*' * length) + '****'
    text = '* ' + string + ' *'
    output = border_top_bot + '\n' + text + '\n' + border_top_bot
    return output


string = input('Enter string: ')
print(border_string(string))
