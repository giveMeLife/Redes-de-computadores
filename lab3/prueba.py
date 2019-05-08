from scipy.misc import imread
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as imgplt

imagen = Image.open("leena512.bmp")

img = np.array(imagen)

kernel = np.array([ [ 1, 4, 6 ,4, 1],
                    [ 4, 16, 24, 16, 4],
                    [ 6, 24, 36, 24, 6],
                    [ 4, 16, 24, 16, 4],
                    [ 1, 4, 6, 4, 1]])

kernel = np.multiply(kernel,1/256)

aux = np.zeros((np.shape(img)[0]+2,np.shape(img)[1]+2),dtype=np.uint8)
for i in range(2,np.shape(aux)[0]):
    for j in range(2, np.shape(aux)[1]):
        aux[i][j] = img[i-2][j-2]


print(np.shape(img))
#imgplot = plt.imshow(imagen)
Image.fromarray(aux).show()
#print(imagen[0][0])
