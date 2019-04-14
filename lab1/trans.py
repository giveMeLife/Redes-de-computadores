import numpy as np
import matplotlib.pyplot as py
import scipy.io.wavfile as wavfile
from scipy.fftpack import fft

############### Grafico de Tiempo ############################

sound = wavfile.read("handel.wav")
py.subplot(4,1,1)
x = np.linspace(0,sound[1].size/sound[0],sound[1].size)
y=sound[1]
py.plot(x,y)
py.xlabel("Tiempo (s)")
py.ylabel("Muestra")

################ Grafico de Frecuencia #######################

sp = np.fft.fft(sound[1])
freq = np.fft.fftfreq(sound[1].size,1/sound[0])
py.subplot(4,1,2)
py.plot(freq,np.absolute(sp))
py.xlabel('Frecuencia')
py.ylabel('Amplitud')

################ Grafico de Frecuencia truncado #######################
copySp = sp.copy()
#print(len(copySp))
for x in range(2000):
	copySp[x] = 0
	copySp[73112 - x] = 0
for x in range(12000,36556):
	copySp[x] = 0
	copySp[73112 - x] = 0
py.subplot(4,1,3)
py.plot(freq,np.absolute(copySp))
py.title("Frecuencia truncada")
py.xlabel('Frecuencia(Hz)')
py.ylabel('Amplitud')

################ Grafico de Frecuencia truncado inversa #######################
inverseSp = np.fft.ifft(copySp).real
py.subplot(4,1,4)
#py.plot(x,inverseSp)
py.title("Frecuencia truncada inversa")
py.xlabel('Tiempo')
py.ylabel('Amplitud')
wavfile.write("test.wav",sound[0],inverseSp)

py.show()