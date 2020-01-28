import numpy as np
from scipy import stats
import scipy.special
import math
import statistics


def func(arr, gamma):
    n = len(arr)
    X = arr.mean()
    D = statistics.stdev(arr)
    print('D: ', D)
    print('X : ', X)
    sigma_v = math.sqrt(n / (n - 1)) * D
    t = round(stats.t.ppf(gamma, df=n - 1), 2)
    print('t: ', t)
    lower = X - (t * sigma_v / math.sqrt(n))
    high = X + (t * sigma_v / math.sqrt(n))
    interval = [lower, high]
    print(interval)


N = 10000
n = 1000
mu = 21
sigma = mu % 5 + 1
gamma = 0.99

array = stats.norm.rvs(loc=mu, scale=sigma, size=N, random_state=None)
arr = np.random.choice(array, n, replace=False)

func(arr, gamma)
