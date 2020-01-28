import random
import math
import statistics
import matplotlib.pyplot as mp

try:
    n = int(input('Enter size of array: '))
    array = []
    for i in range(0, n):
        array.append(random.randint(0, 10))
    array.sort()

    print(array)

    maxValue = max(array)
    minValue = min(array)
    q1_array = []
    q3_array = []

    median = statistics.median(array)
    if n % 2 == 0:
        q1_array = array[0:int(n / 2)]
        q3_array = array[int(n / 2):n]
    else:
        q1_array = array[0:int(n / 2)]
        q3_array = array[int(n / 2) + 1:n]
    Q1 = statistics.median(q1_array)
    Q3 = statistics.median(q3_array)
    IQR = Q3 - Q1
    print('Q1 array: ', q1_array)
    print('Q3 array: ', q3_array)
    print('Median: ', median)
    print('IQR: ', IQR)
    mp.boxplot(array)
    mp.show()
except ValueError:
    print('Please enter a number')
