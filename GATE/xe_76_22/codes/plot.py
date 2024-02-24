import numpy as np
import matplotlib.pyplot as plt
import os

data = np.loadtxt('data.dat')
x = data[:, 0]
y = data[:, 1]

fig,ax = plt.subplots()
ax.plot(x,y)
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$x(t)$')
ax.grid(True)
plt.savefig('../figs/plot.png')
os.system('open ../figs/plot.png')
