import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as imgplt


def aplicarKernel(imagen, kernel):
    aux = np.zeros((np.shape(imagen)[0] + 2, np.shape(imagen)[1] + 2))
    for i in range(2, np.shape(aux)[0]):
        for j in range(2, np.shape(aux)[1]):
            aux[i][j] = imagen[i - 2][j - 2]

    suma = 0
    newImg = np.zeros((np.shape(imagen)[0], np.shape(imagen)[1]))
    for i in range(2, np.shape(aux)[0] - 2):
        # print("Soy i ", i)
        for j in range(2, np.shape(aux)[1] - 2):
            #     print("Soy j ", j)
            b = -2
            for k in range(0, np.shape(kernel)[0]):
                a = -2
                for l in range(0, np.shape(kernel)[1]):
                    #                       print("k,l",k,l)
                    #                       print("a,b",a,b)
                    suma = suma + kernel[k][l] * aux[i + b][j + a]
                    a = a + 1
                b = b + 1
            newImg[i - 2][j - 2] = suma
            suma = 0
    return newImg


def grafico(img,title1,title2):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitudFFT = 20*np.log(np.abs(fshift))
    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title(title1), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitudFFT)
    plt.title(title2), plt.xticks([]), plt.yticks([])
    plt.colorbar()
    plt.show()


# noinspection SpellCheckingInspection
imagen = Image.open("leena512.bmp")

img = np.array(imagen)
imagen.close()
kernelSuave = np.array([[1, 4, 6, 4, 1],
                        [4, 16, 24, 16, 4],
                        [6, 24, 36, 24, 6],
                        [4, 16, 24, 16, 4],
                        [1, 4, 6, 4, 1]])

kernelBordes = np.array([[1, 2, 0, -2, -1],
                         [1, 2, 0, -2, -1],
                         [1, 2, 0, -2, -1],
                         [1, 2, 0, -2, -1],
                         [1, 2, 0, -2, -1]])

kernelSuave = np.multiply(kernelSuave, 1 / 256)
newImgSuave = aplicarKernel(img, kernelSuave)
newImgBorde = aplicarKernel(img, kernelBordes)
newImgBordeNorm = Image.fromarray(newImgBorde.clip(0,255).astype('uint8'))
newImgBordeNormArr = np.array(newImgBordeNorm)

grafico(newImgSuave,"Filtro de suavidad","Transformada de Fourier")
grafico(newImgBorde,"Filtro de borde","Transformada de Fourier")
grafico(newImgBordeNormArr,"Filtro de borde normalizado","Transformada de Fourier")

