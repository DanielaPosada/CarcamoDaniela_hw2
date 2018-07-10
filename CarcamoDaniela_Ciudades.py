import numpy as np
from scipy.fftpack import fft2, fftfreq, ifft2, fftshift
from scipy import ndimage
from scipy.signal import convolve2d
import matplotlib.pylab as plt
from math import hypot, pi, cos, sin
import Image
from PIL import Image
# a. Leer imagenes y guardarlas en arreglos
Barcelona=Image.open('Barcelona.jpg').convert('LA')
Paris=Image.open('Paris.jpg').convert('LA')
frac=Image.open('frac.jpeg').convert('LA')
triangulos = Image.open('triangulos.png').convert('LA')
# b. Hacer una figura con cuatro subplots, uno por cada imagen, y guardarla sin mostrarla en imagenes.pdf
fig = plt.figure()
plt.subplot(2, 2, 1)
plt.imshow(Barcelona,cmap='gray')
plt.title("Barcelona")
plt.autoscale(False)
plt.subplot(2, 2, 2)
plt.imshow(Paris,cmap='gray')
plt.title("Paris")
plt.autoscale(False)
plt.subplot(2, 2, 3)
plt.imshow(frac,cmap='gray')
plt.title("fractal")
plt.autoscale(False)
plt.subplot(2, 2, 4)
plt.imshow(triangulos,cmap='gray')
plt.title("triangulos")
plt.autoscale(False)
plt.savefig('imagenes.pdf')
#c. Obtener la transformada de Fourier de las cuatro imagenes
Barcelona2 = ndimage.imread('Barcelona.jpg', flatten=True)   
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
plt.figure()
emB=20*np.log(np.abs(SBarcelona))
emP=20*np.log(np.abs(SParis))
emfrac=20*np.log(np.abs(Sfrac))
emtri=20*np.log(np.abs(Striangulos))
plt.subplot(2, 2, 1)
plt.imshow(emB, cmap='gray')
plt.title("BarcelonaTF")
plt.autoscale(False)
plt.subplot(2, 2, 2)
plt.imshow(emP,cmap='gray')
plt.title("ParisTF")
plt.autoscale(False)
plt.subplot(2, 2, 3)
plt.imshow(emfrac,cmap='gray')
plt.title("fractalTF")
plt.autoscale(False)
plt.subplot(2, 2, 4)
plt.imshow(emtri,cmap='gray')
plt.title("TriangulosTF")
plt.autoscale(False)
plt.savefig('transformadas.pdf')

#e. Hacer otra grafica con cuatro subplots que correspondan a un corte transversal horizontal en el centro de las graficas de las transformadas de Fourier anteriores, y guardarla sinmostrarla en cortes_transversalespdf
plt.figure(figsize=(18,10))
copiaB=abs(FBarcelona.astype(dtype=np.float))
mitadB=int(copiaB.shape[0]/2)
plt.subplot(2, 2, 1)
plt.plot(copiaB[mitadB,:])
plt.title("BarcelonaTransversal")
plt.autoscale(True)

copiaP=abs(FParis.astype(dtype=np.float))
mitadP=int(copiaP.shape[0]/2)
plt.subplot(2, 2, 2)
plt.plot(copiaP[mitadP,:])
plt.title("ParisTransversal")
plt.autoscale(True)

copiaf=abs(Ffrac.astype(dtype=np.float))
mitadf=int(copiaf.shape[0]/2)
plt.subplot(2, 2, 3)
plt.plot(copiaf[mitadf,:])
plt.title("fractalTransversal")
plt.autoscale(True)

copiat=abs(Ftriangulos.astype(dtype=np.float))
mitadt=int(copiat.shape[0]/2)
plt.subplot(2, 2, 4)
plt.plot(copiat[mitadt,:])
plt.title("TriangulosTransversal")
plt.autoscale(True)

plt.savefig('cortes_transversales.pdf')


#h. Para la imagen Barcelona.jpg, construya un filtro que le permita borrar las vias horizontales del mapa, dejando las verticales. Guarde la imagen obtenida sin vias horizontalesen sin_horizontalespdf.
 

