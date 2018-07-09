import numpy as np
from scipy.fftpack import fft2, fftfreq, ifft2, fftshift
from scipy import ndimage
from scipy.signal import convolve2d
import matplotlib.pylab as plt
import Image
from PIL import Image
# a. Leer imagenes y guardarlas en arreglos
Barcelona=Image.open('Barcelona.jpg').convert('LA')
Paris=Image.open('Paris.jpg').convert('LA')
frac=Image.open('frac.jpeg').convert('LA')
triangulos = Image.open('triangulos.png').convert('LA')
# b. Hacer una figura con cuatro subplots, uno por cada imagen, y guardarla sin mostrarla en imagenes.pdf
fig = plt.figure()
ax = fig.add_subplot(2, 2, 1)
ax.imshow(Barcelona,cmap='gray')
ax.autoscale(False)
ax2 = fig.add_subplot(2, 2, 2)
ax2.imshow(Paris,cmap='gray')
ax2.autoscale(False)
ax3 = fig.add_subplot(2, 2, 3)
ax3.imshow(frac,cmap='gray')
ax3.autoscale(False)
ax4 = fig.add_subplot(2, 2, 4)
ax4.imshow(triangulos,cmap='gray')
ax4.autoscale(False)
plt.savefig('imagenes.pdf')
#c. Obtener la transformada de Fourier de las cuatro imagenes
Barcelona2 = ndimage.imread('Barcelona.jpg', flatten=True)     # flatten=True gives a greyscale image
FBarcelona = fft2(Barcelona2)
SBarcelona=fftshift(FBarcelona )

Paris2 = ndimage.imread('Paris.jpg', flatten=True) 
FParis = fft2(Paris2)
SParis=fftshift(FParis)

frac2 = ndimage.imread('frac.jpeg', flatten=True)    
Ffrac = fft2(frac2)
Sfrac=fftshift(Ffrac)

triangulos2 = ndimage.imread('triangulos.png', flatten=True)  
Ftriangulos = fft2(triangulos2)
Striangulos=fftshift(Ftriangulos)

#d. Hacer una grafica con cuatro subplots correspondientes a las transformadas de Fourier de las cuatro imagenes, y guardarla sin mostrarla en transformadaspdf
fig2 = plt.figure()
emB=20*np.log(np.abs(SBarcelona))
emP=20*np.log(np.abs(SParis))
emfrac=20*np.log(np.abs(Sfrac))
emtri=20*np.log(np.abs(Striangulos))
ay = fig2.add_subplot(2, 2, 1)
ay.imshow(emB, cmap='gray')
ay.autoscale(False)
ay2 = fig2.add_subplot(2, 2, 2)
ay2.imshow(emP,cmap='gray')
ay2.autoscale(False)
ay3 = fig2.add_subplot(2, 2, 3)
ay3.imshow(emfrac,cmap='gray')
ay3.autoscale(False)
ay4 = fig2.add_subplot(2, 2, 4)
ay4.imshow(emtri,cmap='gray')
ay4.autoscale(False)
plt.savefig('transformadas.pdf')

#e. Hacer otra grafica con cuatro subplots que correspondan a un corte transversal horizontal en el centro de las graficas de las transformadas de Fourier anteriores, y guardarla sinmostrarla en cortes_transversalespdf
fig3 = plt.figure()
copiaB=abs(FBarcelona.astype(dtype=np.float))
mitadB=int(copiaB.shape[0]/2)
ax = fig3.add_subplot(2, 2, 1)
ax.plot(copiaB[mitadB,:])
ax.autoscale(True)

copiaP=abs(FParis.astype(dtype=np.float))
mitadP=int(copiaP.shape[0]/2)
ax2 = fig3.add_subplot(2, 2, 2)
ax2.plot(copiaP[mitadP,:])
ax2.autoscale(True)

copiaf=abs(Ffrac.astype(dtype=np.float))
mitadf=int(copiaf.shape[0]/2)
ax3 = fig3.add_subplot(2, 2, 3)
ax3.plot(copiaf[mitadf,:])
ax3.autoscale(True)

copiat=abs(Ftriangulos.astype(dtype=np.float))
mitadt=int(copiat.shape[0]/2)
ax4 = fig3.add_subplot(2, 2, 4)
ax4.plot(copiat[mitadt,:])
ax4.autoscale(True)

plt.savefig('cortes_transversales.pdf')


#h. Para la imagen Barcelona.jpg, construya un filtro que le permita borrar las vias horizontales del mapa, dejando las verticales. Guarde la imagen obtenida sin vias horizontalesen sin_horizontales.pdf.

