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
#barce = plt.imread('Barcelona.jpg').astype(float)
#barce_fft = fft2(barce)

#def plot_spectrum(im_fft):
 #   from matplotlib.colors import LogNorm
    # A logarithmic colormap
  #  plt.imshow(np.abs(im_fft), norm=LogNorm(vmin=5))
   # plt.colorbar()

#plt.figure()
#plot_spectrum(barce_fft)
#plt.title('Fourier transform')

#paris= plt.imread('Paris.jpg').astype(float)
#paris_fft = fft2(paris)

#def plot_spectrum(im_fft):
 #   from matplotlib.colors import LogNorm
    # A logarithmic colormap
  #  plt.imshow(np.abs(im_fft), norm=LogNorm(vmin=5))
   # plt.colorbar()

#plt.figure()
#plot_spectrum(paris_fft)
#plt.title('Fourier transform')

#plt.figure()
image = ndimage.imread('Paris.jpg', flatten=True)     # flatten=True gives a greyscale image
fft2r = fft2(image)
shi=fftshift(fft2r)
plt.figure()
em=20*np.log(np.abs(shi))
plt.imshow(em, cmap='gray')
plt.show()

#f = fft2(Barcelona)
#

#FBarcelona=fft2(Barcelona)
#FParis=fft2(Paris)
#frac=fft2(frac)
#triangulos=fft2(frac)
#d. Hacer una grafica con cuatro subplots correspondientes a las transformadas de Fourier de las cuatro imagenes, y guardarla sin mostrarla en transformadaspdf


#ax2.plot(Paris, cmap='gray')
#ax3.plot(frac, cmap='gray')
#ax4.plot(tri, cmap='gray')
#



#I8 = (((I - I.min()) / (I.max() - I.min())) * 255.9).astype(np.uint8)

#img = Image.fromarray(I8)
#img.save("file.png")


#print(np.shape(img))
