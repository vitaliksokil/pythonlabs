import math


class Star:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


file = open('file.txt', 'r')
stars = []
i = 0
for line in file:
    if i == 0:
        n, a = line.split()
        n, a = int(n), int(a)
    else:
        name, x, y = line.split()
        x, y = int(x), int(y)
        stars.append(Star(name, x, y))
    i += 1
file.close()

a = a * (math.pi / 180)
for star in stars:
    star.x = star.x * math.cos(a) - star.y * math.sin(a)
    star.y = star.y * math.cos(a) + star.x * math.sin(a)

    star.x = round(star.x)
    star.y = round(star.y)

stars.sort(key=lambda star: (star.y, star.x), reverse=False)

new_file = open('result.txt', 'w')
result = ''
for star in stars:
    result += star.name + ' '
new_file.write(result)
new_file.close()
