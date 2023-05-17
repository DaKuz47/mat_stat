import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(42)

# choose distribution
dist = stats.poisson(10)
distName = "Poisson"

sizes = [10, 50, 1000]
results = []

for size in sizes:
    results.append(sorted(dist.rvs(size=size)))

fig, ax = plt.subplots(1, 1)

for i in range(0, 3):
    ax[i].set_ylabel("Density")
    ax[i].set_xlabel(f"{distName.lower()}Number")
    ax[i].set_title(f"{distName}Numbers n = {len(results[i])}")
    ax[i].hist(results[i], bins=20, density=True, edgecolor='black')
    ax[i].plot(results[i], dist.pmf(results[i]))

plt.show()