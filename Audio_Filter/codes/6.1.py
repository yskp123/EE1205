import soundfile as sf
from scipy import signal, fft
import numpy as np
from numpy.polynomial import Polynomial as P
from matplotlib import pyplot as plt


def myfiltfilt(b, a, input_signal):
    input_signal = np.squeeze(input_signal)
    X = np.fft.fft(input_signal)
    w = np.linspace(0, 1, len(X) + 1)
    W = np.exp(2j*np.pi*w[:-1])
    Y = ((np.absolute(np.polyval(b,W)/(np.polyval(a,W))))**2)[:, None]
    return fft.ifft(Y*X).real
#read .wav file 
input_signal,fs = sf.read('song.wav') 
input_signal = np.squeeze(input_signal)
print(len(input_signal))
np.savetxt("in.txt", input_signal)

#sampling frequency of Input signal
sampl_freq=fs

#order of the filter
order=4   

#cutoff frquency 
cutoff_freq=4000.0  

#digital frequency
Wn=2*cutoff_freq/sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 

#filter the input signal with butterworth filter
output_signal = signal.filtfilt(b, a, input_signal,padlen=1)

op1 = myfiltfilt(b, a, input_signal)
x_plt = np.arange(len(input_signal))
#Verify outputs by plotting
plt.plot(x_plt[6000:10000], output_signal[6000:10000,0], 'b.',label='Output by built in function')
plt.plot(x_plt[6000:10000], op1[6000:10000,0], 'r.',label='Output by not using built in function')
plt.title("Verification of outputs of Audio Filter")
plt.grid()
plt.legend()
plt.savefig("../figs/Audio_Filter_verf.png")
