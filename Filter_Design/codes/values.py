import numpy as np

def cN(x, N):
    return np.cosh(N * np.arccosh(x))

Fs = 48e3
r = 11224
sigma = sum(int(digit) for digit in str(r))
j = (r - 11000) % sigma
Fp1 = (4 + 0.6 * (j + 2)) * 1e3
Fp2 = (4 + 0.6 * (j)) * 1e3
w_p1 = 2 * np.pi * Fp1 / Fs
w_p2 = 2 * np.pi * Fp2 / Fs
w_c = (w_p1 + w_p2) / 2
Fs1 = Fp1 + 0.3 * 1e3
Fs2 = Fp2 - 0.3 * 1e3
w_s1 = 2 * np.pi * Fs1 / Fs
w_s2 = 2 * np.pi * Fs2 / Fs
W_p1 = np.tan(w_p1 / 2)
W_p2 = np.tan(w_p2 / 2)
W_s1 = np.tan(w_s1 / 2)
W_s2 = np.tan(w_s2 / 2)
W0 = np.sqrt(W_p1 * W_p2)
B = W_p1 - W_p2
W_Ls1 = (W_s1**2 - W0**2) / (B * W_s1)
W_Ls2 = (W_s2**2 - W0**2) / (B * W_s2)
W_Ls = min(abs(W_Ls1), abs(W_Ls2))
delta = 0.15
D1 = (1/(1 - delta)**2) - 1
D2 = (1/delta**2) - 1

print(f"Fs = {Fs / 1e3} kHz")
print(f"r = {r}")
print(f"sigma = {sigma}")
print(f"j = {j}")
print(f"Fp1 = {Fp1 / 1e3} kHz")
print(f"Fp2 = {Fp2 / 1e3} kHz")
print(f"w_p1 = {w_p1 / np.pi}*pi")
print(f"w_p2 = {w_p2 / np.pi}*pi")
print(f"w_c = {w_c / np.pi}*pi")
print(f"Fs1 = {Fs1 / 1e3} kHz")
print(f"Fs2 = {Fs2 / 1e3} kHz")
print(f"w_s1 = {w_s1 / np.pi}*pi")
print(f"w_s2 = {w_s2 / np.pi}*pi")
print(f"W_p1 = {W_p1}")
print(f"W_p2 = {W_p2}")
print(f"W_s1 = {W_s1}")
print(f"W_s2 = {W_s2}")
print(f"W0 = {W0}")
print(f"B = {B}")
print(f"W_Ls1 = {W_Ls1}")
print(f"W_Ls2 = {W_Ls2}")
print(f"W_Ls = {W_Ls}")
print(f"{np.sqrt(D2)/cN(W_Ls,4)}<epsilon<{np.sqrt(D1)}")
