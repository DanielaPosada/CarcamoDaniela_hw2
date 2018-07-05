import numpy as np
import matplotlib.pylab as plt

n = 128 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 32 ) #32 samples per unit frequency
t = np.linspace( 0,(n-1)*dt, n)

y=np.cos(2*np.pi*f*t) - 0.4*np.sin(2*np.pi*(2*f)*t)


Fourier=np.ones((n),dtype=np.complex64)
suma=0.0
G=0.0
for h in range(n):
	G=0
	for k in range(n):
		G+=y[k]*np.exp(-1j*2.0*np.pi*k*h/n)
	Fourier[h]=G/n




# SU implementacion de la transformada de fourier
print Fourier[0:10]

# Lo siguiente es para verificar que su codigo este bien:
from scipy.fftpack import fft, fftfreq
fft_x = fft(y) / n # FFT Normalized
freq = fftfreq(n, dt) # Recuperamos las frecuencias
print(fft_x[0:10])
plt.plot(freq,abs(Fourier))
#plt.plot(freq,abs(fft_x))
plt.show()


