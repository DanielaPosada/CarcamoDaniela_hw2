import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
# aLea y almacene los datos de Signalcsv
archivo=np.genfromtxt("Signal.csv",delimiter=",",skip_header=0)
# bGrafique la senal original y guarde la grafica sin mostrarla en Signalpdf
plt.figure()
plt.plot(archivo[:,0],archivo[:,1])
plt.savefig('Signal.pdf')
npuntos=archivo[:,1].size
# cImplementacion propia transformada de Fourier
Fourier=np.ones((npuntos),dtype=np.complex64)
for h in range(npuntos):
	G=0.0
	for k in range(npuntos):
		G+=archivo[k,1]*np.exp(-1j*2.0*np.pi*k*h/npuntos)
	Fourier[h]=G/npuntos
# dEncuentre las tres frecuencias principales de la senal
f1=0
f2=0
f3=0
# eImprima un mensaje
#print Las tres frecuencias principales de la senal son: f1 f2 f3
fft_x = fft(archivo[:,1]) / npuntos # FFT Normalizada

#freq = fftfreq(npuntos, dt) # Recuperamos las frecuencias
plt.figure()
plt.plot(abs(Fourier))
plt.show()
#plt.savefig('TF_Signal.pdf')


