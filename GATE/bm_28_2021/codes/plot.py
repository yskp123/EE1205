import numpy as np
import matplotlib.pyplot as plt
import os

t = np.linspace(0, 5, 1000)
x_values = [1, 2, 3]
x = np.array(x_values)
y = np.sin(np.subtract.outer(x, 5*t))

fig, ax = plt.subplots()
line1, = ax.plot(t, y[0])
line2, = ax.plot(t, y[1])
line3, = ax.plot(t, y[2])
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$y(x,t)$')
ax.grid(True)
ax.legend([line1, line2, line3], [f'x={x_values[0]:.2f}', f'x={x_values[1]:.2f}', f'x={x_values[2]:.2f}'], loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3)
plt.savefig('../figs/plot.png')
os.system('open ../figs/plot.png')

