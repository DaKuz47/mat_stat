import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.lines import Line2D

def formatOy(x, pos):
    return f"{sizes[pos]}"


np.random.seed(42)

# choose distribution
#dist = stats.norm
#dist = stats.cauchy
#dist = stats.laplace(loc=0, scale=1/np.sqrt(2))
#dist = stats.poisson(10)
dist = stats.uniform(loc=-np.sqrt(3), scale=2*np.sqrt(3))

sizes = [20, 100]
results = []

for size in sizes:
    results.append(sorted(dist.rvs(size=size)))

fig, ax = plt.subplots(1, 1)

pos = [0.1, 0.3]


box = ax.boxplot([results[0], results[1]], vert=False, positions=pos)
print(f"n = 20: {len(box['fliers'][0].get_data()[0])/20}, n = 100: {len(box['fliers'][1].get_data()[0])/100}")
ax.yaxis.set_major_formatter(FuncFormatter(formatOy))
plt.xlabel("x")
plt.ylabel("n")
plt.show()