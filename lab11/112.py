def gen_rand(x):
    if len(x) != 6:
        exit('X should has 6 numbers, possible with leading zeros ')
    try:
        int(x)
    except ValueError:
        exit('Please enter correct value!!! For example : 654321')
    while True:
        y = x[3:] + x[0:3]
        x_y = str(int(x) * int(y))
        new_val = x_y[(len(x_y) // 2) - 3:len(x_y) // 2] + x_y[len(x_y) // 2:(len(x_y) // 2) + 3]
        yield int(new_val)
        x = str(new_val)


x = input('Enter seed: ')
rand_val = gen_rand(x)
print(next(rand_val))

while True:
    choice = input('1.One more rand\n2.Stop\n')
    if choice == '1':
        print(next(rand_val))
    elif choice == '2':
        break
    else:
        print("Incorrect value!!! Try again!!!")
