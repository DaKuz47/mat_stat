import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def quantile(arr, q):
    n = len(arr) - 1
    if n*q == int(n*q):
        return arr[n*q]
    else:
        return arr[int(n*q) + 1]


def zQ(arr):
    first = quantile(arr, 1/4)
    second = quantile(arr, 3/4)

    return (first + second)/2


np.random.seed(42)

# choose distribution
dist = stats.uniform(loc=-np.sqrt(3), scale=np.sqrt(3)*2)
distName = "normal"

sizes = [10, 50, 1000]

characteristiques = {
    'moment': [[],[],[]],
    'med': [[],[],[]],
    'zR': [[],[],[]],
    'zQ': [[],[],[]],
    'ztr': [[],[],[]],
}

for i in range(1000):
    results = []

    for j in range(len(sizes)):
        results.append(np.sort(dist.rvs(size=sizes[j])))
        characteristiques['moment'][j].append(results[j].mean())
        characteristiques['med'][j].append(np.median(results[j]))
        characteristiques['zR'][j].append((results[j][0] + results[j][sizes[j]-1])/2)
        characteristiques['zQ'][j].append(zQ(results[j]))
        characteristiques['ztr'][j].append(stats.trim_mean(results[j], 0.25))

f = open("table.txt", "w")

for j in range(3):
    Es = []
    Ds = []
    f.write("\\hline\n")
    f.write(f"n = {sizes[j]} & & & & & \\\\\n")
    f.write("& $\\overline{x}$ & $med x$ & $z_R$ & $z_Q$ & $z_{tr}$\\\\\\hline\n$E(z)$")
    for res in characteristiques.values():
        Es.append(np.mean(res[j]))
        Ds.append(np.mean([x**2 for x in res[j]]) - np.mean(res[j])**2)

    for i in range(len(Es)):
        f.write(f" & ${toFixed(Es[i], 4)}$")
    f.write("\\\\\n$D(z)$")

    for i in range(len(Ds)):
        f.write(f" & ${toFixed(Ds[i], 4)}$")
    f.write("\\\\\n$E\\pm \\sqrt{D}$")
    
    for i in range(len(Ds)):
        f.write(f" & ${toFixed(Es[i], 4)}\\pm {toFixed(np.sqrt(Ds[i]), 4)}$")
    f.write("\\\\")



