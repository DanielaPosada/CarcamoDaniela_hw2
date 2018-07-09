import numpy as np
import matplotlib.pylab as plt
import scipy.io.wavfile as wav
from scipy.fftpack import fft, fftfreq
from scipy.signal import convolve2d
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
a, b=Barcelona.size

#d. Hacer una grafica con cuatro subplots correspondientes a las transformadas de Fourier de las cuatro imágenes, y guardarla sin mostrarla en transformadaspdf

#ax2.plot(Paris, cmap='gray')
#ax3.plot(frac, cmap='gray')
#ax4.plot(tri, cmap='gray')
#



#I8 = (((I - I.min()) / (I.max() - I.min())) * 255.9).astype(np.uint8)

#img = Image.fromarray(I8)
#img.save("file.png")


#print(np.shape(img))
