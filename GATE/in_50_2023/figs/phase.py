import matplotlib.pyplot as plt
import numpy as np
import os

# Define your transfer function G(s)
def G(s):
    # Example transfer function |G(s)| = 1 / (s^2 + 1)
    return 2*(1-s)/(1+s)**2

# Define the range of frequencies (w)
w_values = np.logspace(-2, 3, 1000)  # From 0.01 to 1000

# Compute phase for each frequency (in degrees) using np.angle
G_phase = np.angle(G(1j * w_values), deg=True)

# Unwrap the phase to avoid phase wrapping
G_phase_unwrapped = np.unwrap(G_phase * np.pi / 180) * 180 / np.pi
log_w_values = np.log(w_values)

# Plot phase of G(s) vs log(w)
fig,ax = plt.subplots()
plt.plot(log_w_values, G_phase_unwrapped)
plt.scatter(np.log(np.sqrt(3)), -180, color='red', marker='s', s=20, label='PM=0')
plt.xlabel(r'$\log\omega$')
plt.ylabel(r'$\angle G(j\omega)$')
plt.grid(True)
plt.legend()
ax.set(yticks=np.linspace(-300,0,6))
plt.savefig('../figs/phase.png')
os.system('open ../figs/phase.png')
