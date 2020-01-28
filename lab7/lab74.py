def simple_crypt(string):
    crypt_string = ''
    for i in string:
        crypt_string += chr(ord(i) + 1)
    return crypt_string


string = input('Enter string: ')
print(simple_crypt(string))
