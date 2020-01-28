import math
from decimal import Decimal
import statistics
import matplotlib.pyplot as plt
import numpy as np


def print_table(intervals, fi, wi, fic, wic, xmi, Mo, Me):
    print('-' * 153)
    print('N\t|\tintervals\t|\tfi\t|\twi\t|\tfiс\t|\twic\t|\txmi\t\t|Mo       \t|Me       \t|')
    print('-' * 153)
    for i in range(0, len(intervals)):
        print(i, '\t|', intervals[i], '   \t|\t', fi[i], '\t|\t', str(wi[i])[:5], '\t|\t', fic[i], '\t|\t', str(wic[i])[:5], '\t|\t',
              xmi[i], '   \t|', Mo[i], '    \t|', Me[i], '    \t|\t', )
    print('-' * 153)
    print('\t|\t', '\t', '\t|\t', sum(fi), '\t|\t', sum(wi), '\t|\t', )
    print('-' * 153)


def create_table(arr):
    arr = sorted(arr)
    r = 1 + 3.322 * math.log10(len(arr))
    d = round(Decimal((max(arr) - min(arr)) / r), 2)
    print('r: ', round(r))
    print('d: ', d)

    # creating intervals
    intervals = []
    temp = round(Decimal(arr[0]), 2)
    # intervals from 0 to second last
    for i in range(0, round(r) - 1):
        intervals.append([float(temp), float(temp + d)])
        temp = round(Decimal(temp + d), 2)
    intervals.append([float(temp), round(arr[-1],2)])  # adding the last one element

    # creating fi array
    interval_number = 0
    fi = []
    count = 0
    for i in arr:
        if intervals[interval_number][0] <= round(i, 2) < intervals[interval_number][1]:
            count += 1
        else:
            fi.append(count)
            count = 1
            interval_number += 1
        # the last element should be added, because it doesn't meet the condition, because it takes range [x,x+d)
        if i == arr[-1]:
            fi[-1] += 1
    # creating wi
    wi = []
    for i in fi:
        wi.append(i / len(arr))

    # creating fiс and wic (f cumulative)
    fic = [fi[0]]  # adding first element
    wic = [wi[0]]
    for i in range(1, len(fi)):
        fic.append(fic[i - 1] + fi[i])
        wic.append(wic[i - 1] + wi[i])

    # creating xmi (the middle of the i-th interval )
    xmi = []
    for i in intervals:
        temp_sum = Decimal(str(i[0])) + Decimal(str(i[1]))
        xmi.append(temp_sum / Decimal(str(len(i))))

    # 4. calculating x average
    fi_xmi_mult = []
    for i in range(0, len(fi)):
        fi_xmi_mult.append(fi[i] * xmi[i])
    X_ = sum(fi_xmi_mult) / sum(fi)  # x average
    print('x average: ', X_)

    # 5. calculating Mo and Me
    Mo = []
    Me = []
    i = 0
    for interval in intervals:
        f_prev = 0 if i == 0 else fi[i - 1]
        f_next = 0 if i == len(fi) - 1 else fi[i + 1]
        f_cur = fi[i]
        S = 0 if i == 0 else fic[i - 1]
        try:
            Me.append(round(Decimal(str(interval[0])) + d * Decimal(
                str((1 / 2 * sum(fi) - S) / f_cur)), 3))
        except ZeroDivisionError:
            Me.append(0)
        try:
            Mo.append(round(Decimal(str(interval[0])) + d * Decimal(
                str(((f_cur - f_prev) / ((f_cur - f_prev) + (f_cur - f_next))))), 3))
        except ZeroDivisionError:
            Mo.append(0)
        i += 1
    print_table(intervals, fi, wi, fic, wic, xmi, Mo, Me)
    # plt.hist(arr, bins=len(intervals), density=True)
    x_lower = []
    for i in intervals:
        x_lower.append(i[0])
    plt.plot(x_lower, wic)
    plt.hist(arr, bins=len(intervals), density=True, cumulative=True)
    plt.show()

    # 6.  asymmetry coefficient and kurtosis
    xi_fi = []
    for i in range(0, len(intervals)):
        xi_fi.append(fi[i] * xmi[i])
    print('xi_fi: ', xi_fi)
    xa_weight = sum(xi_fi) / len(arr)
    # product = ((xi-xa_weight)**2) * fi
    product_2 = []
    product_3 = []
    product_4 = []
    for i in range(0, len(intervals)):
        product_2.append(((xmi[i] - xa_weight) ** 2) * fi[i])
        product_3.append(((xmi[i] - xa_weight) ** 3) * fi[i])
        product_4.append(((xmi[i] - xa_weight) ** 4) * fi[i])
    # D = sum((xmi[i] - xa_weight)**2) * fi[i]) / n
    D = sum(product_2) / len(arr)
    sigma = math.sqrt(D)
    m3 = sum(product_3) / len(arr)
    m4 = sum(product_4) / len(arr)
    A = round(m3 / Decimal(str(sigma ** 3)), 3)
    E = round((m4 / Decimal(str(sigma ** 4))) - 3, 3)
    print('The asymmetry coefficient: ', A)
    print('The excess coefficient: ', E)


arr = [4.21, 5.22, 2.84, -0.2, 6.37, -0.54, -3.71, 2.77, 6.35, 5.88, 3.99, -1.25, -4.38, -3.5, -2.4, 4.51, -1.43, -4.47,
       4.01, 5.33, 2.61, 3.8, 2.35, -2.49, -2.16, 2.06, -2.13, 3.03, 6.59, 2.13]
mu = 20
sig = 5
n = 60 * 10
task2_arr = np.random.normal(mu, sig, n)
create_table(arr)
