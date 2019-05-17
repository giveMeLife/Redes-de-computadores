import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as imgplt

#Entrada: Matriz que representa la imagen y el kernel a aplicar.
#Procedimiento: Crea una matriz con dos filas y columnas que la imagen original, para luego copiar la información de la imagen en esta matriz,
#               logrando asi que la imagen tenga un borde.
#               Se le aplica el kernel a la matriz con borde, donde el resultado se guarda en una matriz de ceros que tiene el mismo tamaño que la 
#               imagen original.
#               Cabe destacar que la posicion en la matriz con borde de los pixeles con informacion importante esta corrido en 2, tanto para fila como 
#               columna.
#Salida: Matriz resultante tras aplicar el kernel.
def aplicarKernel(imagen, kernel):
    aux = np.zeros((np.shape(imagen)[0] + 2, np.shape(imagen)[1] + 2))
    for i in range(2, np.shape(aux)[0]):
        for j in range(2, np.shape(aux)[1]):
            aux[i][j] = imagen[i - 2][j - 2]

    suma = 0
    newImg = np.zeros((np.shape(imagen)[0], np.shape(imagen)[1]))
    for i in range(2, np.shape(aux)[0] - 2):
        for j in range(2, np.shape(aux)[1] - 2):
            b = -2
            for k in range(0, np.shape(kernel)[0]):
                a = -2
                for l in range(0, np.shape(kernel)[1]):
                    suma = suma + kernel[k][l] * aux[i + b][j + a]
                    a = a + 1
                b = b + 1
            newImg[i - 2][j - 2] = suma
            suma = 0
    return newImg

#Entrada:n Matriz que contiene la información de la imagen y título de los gráficos.
#Procedimiento: Calcula la transformada de Fourier para la matriz ingresada, ademas de centrar el cero de la imagen. 
#               Grafica en conjunto la imagen ingresada y su transformada de Fourier.
#Salida:
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

##########################Bloque Principal###################################
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

#Normalizacion de las imágenes.
newImgSuaveNorm = Image.fromarray(newImgSuave.clip(0,255).astype('uint8'))
newImgBordeNorm = Image.fromarray(newImgBorde.clip(0,255).astype('uint8'))
newImgSuaveNorm.save("suave.png")
newImgBordeNorm.save("borde.png")

grafico(newImgSuaveNorm,"Filtro de suavidad","Transformada de Fourier")
grafico(newImgBordeNorm,"Filtro de borde","Transformada de Fourier")
