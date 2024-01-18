import matplotlib.pyplot as plt
import numpy as np
n_values = list(range(8))
x=1.3
y_values = [x ** (2*i+3) for i in n_values]
fig,ax = plt.subplots()
ax.stem(n_values,y_values,label=f'x={x}')
ax.set(xlim=(-1,8), xticks=np.arange(0,8),ylim=(0,90),yticks=np.arange(0,90,5))
plt.xlabel('n')
plt.ylabel('x(n)')
plt.legend()
plt.title(f'Plot of $x(n)$ for $x={x}$')
plt.grid(True)
plt.savefig('plot_3.png')
