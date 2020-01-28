def sort_by_length(string):
    string = string.split()
    string = sorted(string, key=len)
    string = ' '.join(string)
    return string


string = input('Enter string: ')
print(sort_by_length(string))
