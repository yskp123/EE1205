import numpy as np

file_path = "data.dat"
data = np.loadtxt(file_path)

n_values = data[:, 0]
x = data[:, 1]

print(np.sum(x))

