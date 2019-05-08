from scipy.misc import imread
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as imgplt
from PIL import Image

imagen = Image.open("leena512.bmp")
matrizImagen = np.array(imagen)
print(matrizImagen)
kernel = np.array([ [ 1, 4, 6 ,4, 1],
                    [ 4, 16, 24, 16, 4],
                    [ 6, 24, 36, 24, 6],
                    [ 4, 16, 24, 16, 4],
                    [ 1, 4, 6, 4, 1]])

kernel = np.multiply(kernel,1/256)

aux = np.zeros((512,512,3),dtype=np.uint8)
for i in range(2,512):
    for j in range(2, 512):
        aux[i][j][0] = imagen[i][j][0]
        aux[i][j][1] = imagen[i][j][1]
        aux[i][j][2] = imagen[i][j][2]

#print(imagen[0][0])'''
