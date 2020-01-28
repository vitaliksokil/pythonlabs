import matplotlib.pyplot as plt
import statistics


def multiply_lists(list1, list2):
    if len(list1) != len(list2):
        exit('Lists lengths should be equal')
    result_list = []
    for i in range(0, len(list1)):
        result_list.append(list1[i] * list2[i])
    return result_list


# returning point y:x
def linear_regression_equation(b0, b1, x):
    y_points = []
    for i in x:
        y_points.append(b0 + b1 * i)
    return y_points


# x = [2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9]
# y = [2.4, 2.7, 2.9, 3.1, 3.3, 3.4, 3.6, 3.8, 3.9, 4, 4.2, 4.3, 4.4, 4.5, 4.6]
x = [5250, 7620, 940, 1160, 480, 300, 240, 195, 150, 140]
y = [21, 46, 9, 8, 3, 6, 4, 2, 2, 2]
XY_ = statistics.mean(multiply_lists(x, y))
X_ = statistics.mean(x)
Y_ = statistics.mean(y)
X2_ = statistics.mean(multiply_lists(x, x))

b1 = (XY_ - X_ * Y_) / (X2_ - X_ ** 2)
b0 = Y_ - b1 * X_

# y = b0 + b1*x
# 30 - b0 = b1*x;
# x = (30-b0)/b1
equation = linear_regression_equation(b0, b1, x)

print((30-b0)/b1)

plt.scatter(x, y, label='', color='red')
plt.plot(x, equation, label='equation', color='b')
plt.xlabel('Xi')
plt.ylabel('Yi')
plt.title('The points of dependence of the values of Xi and Yi\n and linear regression equation')

plt.show()
