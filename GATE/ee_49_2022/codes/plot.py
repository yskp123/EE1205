import numpy as np
import matplotlib.pyplot as plt
import os

data = np.loadtxt('data.dat')
n = data[:, 0]
x = data[:, 1]

fig,ax = plt.subplots()
ax.stem(n,x)
ax.set_xlabel(r'$n$')
ax.set_ylabel(r'$x[n]$')
ax.grid(True)
plt.savefig('../figs/plot.png')
os.system('open ../figs/plot.png')
