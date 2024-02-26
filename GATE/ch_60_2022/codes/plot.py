import numpy as np
import matplotlib.pyplot as plt
import os

data = np.loadtxt('data.dat')
t = data[:, 0]
y = data[:, 1]

fig,ax = plt.subplots()
ax.plot(t,y)
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$y(t)$')
ax.set(xticks=np.arange(0,7.5,0.5))
ax.grid(True)
plt.savefig('../figs/plot.png')
os.system('open ../figs/plot.png')
