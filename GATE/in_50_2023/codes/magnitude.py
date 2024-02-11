import matplotlib.pyplot as plt
import numpy as np
import os

# Define your transfer function G(s)
def G(s):
    # Example transfer function |G(s)| = 1 / (s^2 + 1)
    return 2*(1-s)/(1+s)**2

# Define the range of frequencies (w)
w_values = np.logspace(-2, 3, 1000)  # From 0.01 to 1000

# Compute |G(s)| for each frequency
G_magnitude = np.abs(G(1j * w_values))  # G(s) evaluated at s = jw

log_w_values = np.log(w_values)
# Plot |G(s)| vs log(w)
plt.figure()
plt.plot(log_w_values, G_magnitude)
plt.xlabel('log(w)')
plt.ylabel('|G(s)|')
plt.grid(True)
plt.savefig('../figs/magnitude.png')
os.system('open ../figs/magnitude.png')
