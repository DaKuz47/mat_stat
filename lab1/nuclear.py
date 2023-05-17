import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

def resize_interval(arr, a, b):
    nevv_interval = [x for x in arr if x >= a and x <= b]

    return nevv_interval

# choose distribution
#dist = stats.norm
#dist = stats.cauchy
#dist = stats.laplace(loc=0, scale=1/np.sqrt(2))
#dist = stats.poisson(10)
dist = stats.uniform(loc=-np.sqrt(3), scale=2*np.sqrt(3))

sizes = [20, 60, 100]
coef = [0.5, 1, 2]
titles = ['$h=h_n/2$', '$h=h_n$', '$h=2h_n$']

results = []
a, b = (-4, 4)
inter = np.arange(a, b, 0.01)

for size in sizes:
    results.append(resize_interval(sorted(dist.rvs(size=size)), a, b))

fig, ax = plt.subplots(1, 3)

i = 1
for j in range(3):
    ax[j].set_xlabel('x')
    ax[j].set_ylabel('f(x)')
    ax[j].set_title(f"{titles[j]}")
    ax[j].set_xlim([a, b])
    ax[j].set_ylim([0, 1])

    kde = stats.gaussian_kde(results[i], bw_method='silverman')
    h_n = kde.factor

    ax[j].plot(inter, dist.pdf(inter))
    sns.kdeplot(results[i], ax=ax[j], bw=h_n*coef[j])

plt.show()