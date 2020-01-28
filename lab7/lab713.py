def is_creatable(string1, string2):
    str1_set = set(string1)
    for str1 in str1_set:
        if str1 not in string2:
            return False
    else:
        return True


string1 = input('Enter 1 string: ')
string2 = input('Enter 2 string: ')
print(is_creatable(string1, string2))
