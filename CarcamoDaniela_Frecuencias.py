import numpy as np
import matplotlib.pyplot as plt
# a. Lea y almacene los datos de Signalcsv
archivo=np.genfromtxt("Signal.csv",delimiter=",",skip_header=0)
# b. Grafique la senal original y guarde la grafica sin mostrarla en Signalpdf
plt.figure()
plt.plot(archivo[:,0],archivo[:,1])
plt.savefig('Signal.pdf')
# c. Implementacion propia transformada de Fourier
npuntos=archivo[:,1].size
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

nuevo1=Fourier.astype(dtype=np.complex64)
f1=0
f2=0
f3=0
for i in range(npuntos):
	if(f1<nuevo1[i]):
		f1=frecuencias[i]
	if(f2<nuevo1[i] and frecuencias[i]!=f1):
		f2=frecuencias[i]
	if(f3<nuevo1[i] and frecuencias[i]!=f2 and frecuencias[i]!=f1):
		f3=frecuencias[i]
maximo1=nuevo1.max()
for h in range(npuntos):
	if(nuevo1[h]==maximo1):
		nuevo1[h]=0
		nuevo1[-h]=0
maximo2=nuevo1.max()
for h in range(npuntos):
	if(nuevo1[h]==maximo2):
		nuevo1[h]=0
		nuevo1[-h]=0
maximo3=nuevo1.max()
for h in range(npuntos):
	if(nuevo1[h]==maximo3):
		f3=frecuencias[h]
	

#e. Imprima un mensaje con las tres frecuencias
print 'Las tres frecuencias principales de la senal son:', f1, f2, f3
#d. Grafique la transformada de Fourier de la senal original y guarde la grafica sin mostrarla
plt.figure()
plt.plot(frecuencias,abs(Fourier))
plt.show()
#plt.savefig('TF_Signal.pdf')
#f. Haga un filtro pasa bajos usando como frecuencia de corte fc=1000
nuevo=Fourier.astype(dtype=np.complex64)
for i in range(frecuencias.size):
	if (abs(frecuencias[i])>=1000):
		nuevo[i]=0
#g.Grafique la senal original y la Senal Filtrada. 
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
ax1.plot(frecuencias,abs(Fourier))
ax2.plot(frecuencias,abs(nuevo))
plt.savefig('SignalFiltro.pdf')






