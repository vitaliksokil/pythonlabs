import random
import math

try:
    n = int(input('Enter number of points: '))
    points = []
    m = 0
    radius = 1

    for i in range(0, n):
        points.append({'x': random.uniform(0, 2), 'y': random.uniform(0, 2)})
        if ((points[i]['x'] - 1) ** 2 + (points[i]['y'] - 1) ** 2) <= radius ** 2:
            m += 1

    res = 4 * m / n

    eps = math.fabs(res - math.pi)
    aeps = (eps / math.pi) * 100

    print('m: ', m)
    print('Res: ', res)
    print('aeps: ', aeps)

except ValueError:
    print('Please enter a number')
