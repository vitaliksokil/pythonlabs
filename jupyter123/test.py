import numpy as np
n = 10
p = 3
Z = np.zeros((n,n))
np.put(Z,np.random.choice(range(n*n),p,replace=False),1)
print(Z)

