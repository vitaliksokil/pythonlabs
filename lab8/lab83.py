import random


def average_and_median(array):
    array.sort()
    n = len(array)
    median = 0
    if n % 2 == 0:
        median = (array[(n // 2) - 1] + array[n // 2]) / 2
    else:
        median = array[n // 2]
    sum = 0
    for item in array:
        sum += item
    average = sum / len(array)
    print('Average: ', average)
    print('Median: ', median)


array = []
try:
    n = int(input('Enter size of array: '))
    for i in range(0, n):
        array.append(random.randint(0, 100))
    array.sort()
    print(array)
    average_and_median(array)
except ValueError:
    print('Please enter integer size of array!!!')
