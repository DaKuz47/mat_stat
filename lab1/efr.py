import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def resize_interval(arr, a, b):
    nevv_interval = [x for x in arr if x >= a and x <= b]

    return nevv_interval


np.random.seed(42)

# choose distribution
#dist = stats.norm
#dist = stats.cauchy
#dist = stats.laplace(loc=0, scale=1/np.sqrt(2))
#dist = stats.poisson(10)
dist = stats.uniform(loc=-np.sqrt(3), scale=2*np.sqrt(3))


a, b = (-4, 4)

sizes = [20, 60, 100]
results = []

for size in sizes:
    results.append(resize_interval(sorted(dist.rvs(size=size)), a, b))


fig, ax = plt.subplots(1, 3)

for i in range(0, 3):
    ax[i].set_xlabel('x')
    ax[i].set_ylabel('F(x)')
    ax[i].set_title(f"n = {sizes[i]}")
    ax[i].plot([-4] + results[i] + [4], [0] + list(dist.cdf(results[i])) + [1])
    ax[i].hist([-4] + results[i]+ [4], density=True, histtype='step', cumulative=True, bins=len(results[i])+2)

plt.show()