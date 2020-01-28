import re


def to_roman(string):
    if re.match(r'\d', string):
        if int(string) > 3999:
            exit('Number should be in diapason 1-3999!!!!')
        roman_numbers_table = {
            '1': 'I',
            '4': 'IV',
            '5': 'V',
            '9': 'IX',
            '10': 'X',
            '40': 'XL',
            '50': 'L',
            '90': 'XC',
            '100': 'C',
            '400': 'CD',
            '500': 'D',
            '900': 'CM',
            '1000': 'M',
        }
        parsed_data = []  # thousands,hundreds,tens,units
        num_of_zeros = len(string) - 1
        # parsing string data to components
        for i in string:
            item_to_add = int(i + '0' * num_of_zeros)
            if item_to_add > 0:
                parsed_data.append(str(item_to_add))
            num_of_zeros -= 1
        num_of_zeros = len(string) - 1
        result = ''
        for item in parsed_data:
            count_of_key_repeat = int(item[0])
            key = str(int(item) // count_of_key_repeat)
            if item in roman_numbers_table:
                result += roman_numbers_table[item]
                num_of_zeros -= 1
            else:
                if count_of_key_repeat > 5:
                    key = str('5' + '0' * num_of_zeros)
                    result += roman_numbers_table[key]
                    count_of_key_repeat = str(count_of_key_repeat - 5)
                    key = str('1' + '0' * num_of_zeros)
                    result += roman_numbers_table[key] * int(count_of_key_repeat)
                else:
                    result += roman_numbers_table[key] * count_of_key_repeat
                num_of_zeros -= 1

        return result
    else:
        roman_numbers_table = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        result = 0
        key = ''
        i = 0
        while i < len(string):
            if i < len(string) - 1:
                key = string[i] + string[i + 1]
                if key in roman_numbers_table:
                    result += roman_numbers_table[key]
                    i += 2
                    continue
            if string[i] in roman_numbers_table and key not in roman_numbers_table:
                result += roman_numbers_table[string[i]]
            i += 1
        return result


string = input('Enter number in diapason 1-3999: ')
print(to_roman(string))
