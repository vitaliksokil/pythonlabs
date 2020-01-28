def shortest_word(string):
    string = string.split()
    return min(string, key=len)


string = input('Enter string: ')
print(shortest_word(string))
