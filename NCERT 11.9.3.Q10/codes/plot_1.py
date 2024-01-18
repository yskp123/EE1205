import matplotlib.pyplot as plt
import numpy as np
n_values = list(range(10))
x=1.1
y_values = [x ** (2*i+3) for i in n_values]
fig,ax = plt.subplots()
ax.stem(n_values,y_values,label=f'x={x}')
ax.set(xlim=(-1,10), xticks=np.arange(0,10),ylim=(0,8),yticks=np.arange(1,8))
plt.xlabel('n')
plt.ylabel('x(n)')
plt.legend()
plt.title(f'Plot of $x(n)$ for $x={x}$')
plt.grid(True)
plt.savefig('plot_1.png')
