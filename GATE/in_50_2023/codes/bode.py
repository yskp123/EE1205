import matplotlib.pyplot as plt
import numpy as np
import os

# Define transfer function G(s)
def G(s):
    return 2*(1-s)/(1+s)**2

# Define the range of frequencies (w)
w_values = np.logspace(-2, 3, 1000)  # From 0.01 to 1000

# Compute |G(s)| for each frequency
G_magnitude = np.abs(G(1j * w_values))  # G(s) evaluated at s = jw

# Compute phase for each frequency (in degrees) using np.angle
G_phase = np.angle(G(1j * w_values), deg=True)

# Unwrap the phase to avoid phase wrapping
G_phase_unwrapped = np.unwrap(G_phase * np.pi / 180) * 180 / np.pi

log_w_values = np.log(w_values)

# Create subplots for magnitude and phase
fig, (ax1, ax2) = plt.subplots(2, 1)

# Plot |G(s)| vs log(w) on the first subplot
ax1.plot(log_w_values, G_magnitude)
ax1.set_xlabel(r'$\log(\omega)$')
ax1.set_ylabel(r'$|G(j\omega)|$')
ax1.grid(True)

# Plot phase of G(s) vs log(w) on the second subplot
ax2.plot(log_w_values, G_phase_unwrapped)
ax2.scatter(np.log(np.sqrt(3)), -180, color='red', marker='s', s=20, label='PM=0')
ax2.set_xlabel(r'$\log(\omega)$')
ax2.set_ylabel(r'$\angle G(j\omega)$')
ax2.grid(True)
ax2.legend()
ax2.set(yticks=np.linspace(-300,0,6))

plt.tight_layout()  # Adjust subplots to prevent overlap
plt.savefig('../figs/bode.png')
os.system('open ../figs/bode.png')

