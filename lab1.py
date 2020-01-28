import random
import statistics
import math
try:
    n = int(input('Enter size of array: '))
    array = []
    for i in range(0, n):
        array.append(random.randint(0, 50))
    array.sort()
    print(array)
    count = 0
    modeCount = 0

    temp = array[0]
    for i in range(1, n):
        if temp == array[i]:
            count += 1
        else:
            if count > modeCount:
                modeCount = count
                mode = temp

            count = 0
            temp = array[i]
    print('PYTHON mode : ', statistics.mode(array))
    print("Mode: ", mode)

    median = 0
    if n % 2 == 0:
        median = (array[int(n / 2) - 1] + array[int(n / 2)]) / 2
    else:
        median = array[int(n / 2)]

    average = sum(array) / n

    print('PYTHON median: ', statistics.median(array))
    print('Median: ', median)

    print('Avarage: ', average)
    print('python Avarage: ', statistics.mean(array))
    summ = 0
    for i in range(0, len(array)):
        summ += (array[i] - average) ** 2
    D = summ / (n - 1)
    print('Variance:', D)
    print('PYTHON variance: ', statistics.variance(array))

    # відхилення
    print('The standard deviation: ', math.sqrt(D))
    print('PYTHON deviation: ', statistics.stdev(array))
except ValueError:
    print('Please, enter a number!!!')
