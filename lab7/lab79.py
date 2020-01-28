def is_lucky(string):
    string = string.strip()
    first_part = string[:len(string) // 2]
    second_part = string[len(string) // 2:]
    if len(string) % 2 != 0:
        second_part = string[len(string) // 2 + 1:]

    first_sum = 0
    for i in first_part:
        first_sum += int(i)

    second_sum = 0
    for i in second_part:
        second_sum += int(i)

    return first_sum == second_sum


string = input('Enter number of ticket:  ')
print(is_lucky(string))
