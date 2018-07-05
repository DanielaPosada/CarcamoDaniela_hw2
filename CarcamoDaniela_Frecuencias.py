import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
# a. Lea y almacene los datos de Signalcsv
archivo=np.genfromtxt("Signal.csv",delimiter=",",skip_header=0)
# b. Grafique la senal original y guarde la grafica sin mostrarla en Signalpdf
#plt.figure()
#plt.plot(archivo[:,0],archivo[:,1])
#plt.savefig('Signal.pdf')
npuntos=archivo[:,1].size
# c. Implementacion propia transformada de Fourier
Fourier=np.ones((npuntos),dtype=np.complex64)
for h in range(npuntos):
	G=0.0
	for k in range(npuntos):
		G+=archivo[k,1]*np.exp(-1j*2.0*np.pi*k*h/npuntos)
	Fourier[h]=G/npuntos
#d. Encuentre las tres frecuencias principales de la senal
frecuencias=np.ones((npuntos))
j=npuntos/2
for k in range(0,npuntos/2):
	frecuencias[k]=(npuntos/2)-j
	j=j-1
j=0
for k in range(npuntos/2,npuntos):
	frecuencias[k]=-((npuntos/2)-j)
	j=j+1
frecuencias=frecuencias/(0.0284040178571)
f1=2
f2=3
f3=1
#e. Imprima un mensaje con las tres frecuencias
print 'Las tres frecuencias principales de la senal son:', f1, f2, f3


fft_x = fft(archivo[:,1]) / npuntos # FFT Normalizada

freq = fftfreq(npuntos, 0.0284040178571/npuntos) # Recuperamos las frecuencias
print freq[-10::]
print frecuencias[-10::]
plt.figure()
plt.plot(freq,abs(fft_x))
plt.figure()
plt.plot(frecuancias,abs(Fourier))
#plt.show()
#plt.savefig('TF_Signal.pdf')


