def shift(string, k):
    if k > len(string) / 2:
        exit('k should be less then half of string length')
    if k > 0:
        new_string = string[k:] + string[0:k]
    elif k < 0:
        new_string = string[k:-1] + string[-1] + string[:k]
    else:
        exit('Value of shift should be less or greater than 0')
    return new_string


string = input('Enter string: ')
try:
    k = int(input('Enter k(number of shift): '))
    print(shift(string, k))
except ValueError:
    exit('k should be an integer!!!')
