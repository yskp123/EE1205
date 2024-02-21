import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import os

tau = 1
K = 1/np.sqrt(2)
# Define the transfer function coefficients
num = [K*(tau**2),2*tau*K,K-(K**3)]
den = [tau**3, 3*(tau**2), 3*tau-2*(K**2)*tau,1-2*(K**2)]

# Create the transfer function H(s) = num(s) / den(s)
sys = signal.TransferFunction(num, den)

# Generate frequency response
w, mag, phase = signal.bode(sys)

log_w = np.log(w)

# Plot magnitude and phase responses
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(log_w, mag)
plt.grid(True)
plt.xlabel(r'$\log(\omega)$')
plt.ylabel(r'$|T(j\omega)|$')

plt.subplot(2, 1, 2)
plt.plot(log_w, phase)
plt.grid(True)
plt.xlabel(r'$\log(\omega)$')
plt.ylabel(r'$\angle T(j\omega)$')

plt.tight_layout()
plt.savefig('../figs/plot_ek.png')
os.system('open ../figs/plot_ek.png')
