import numpy as np
from scipy import stats
import scipy.special
import math

N = 100000
n = 1000
a = 10
sigma = 5
gamma = 0.95

array = stats.norm.rvs(loc=a, scale=sigma, size=N, random_state=None)
arr = np.random.choice(array, n, replace=False)
X = arr.mean()

t = round(stats.norm.ppf(1 - ((1-gamma)/2)),2)
print(t)

lower = X - (t * sigma / math.sqrt(n))
high = X + (t * sigma / math.sqrt(n))
interval = [lower, high]
print('X : ', X)
print(interval)
