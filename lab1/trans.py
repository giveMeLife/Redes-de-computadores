import numpy as np
import matplotlib.pyplot as py
import scipy.io.wavfile as wavfile
from scipy.fftpack import fft


def readFile(nombre):
	############### Grafico de Tiempo ############################
	sound = wavfile.read(nombre)
	'''py.subplot(4,1,1)
	x = np.linspace(0,sound[1].size/sound[0],sound[1].size)
	y=sound[1]
	py.plot(x,y)
	py.xlabel("Tiempo (s)")
	py.ylabel("Muestra")'''
	return sound


def frecuenciaFourier(sound):
################ Grafico de Frecuencia #######################
	transformada = np.fft.fft(sound[1])
	freq = np.fft.fftfreq(sound[1].size,1/sound[0])
	py.subplot(4,1,2)
	py.plot(freq,np.absolute(transformada))
	py.xlabel('Frecuencia')
	py.ylabel('Amplitud')
	return transformada,freq

def frecuenciaFourierTruncado(transformada):
	################ Grafico de Frecuencia truncado #######################
	copyT = transformada.copy()
	#print(len(copyT))
	for x in range(2000):
		copyT[x] = 0
		copyT[73112 - x] = 0
	for x in range(12000,36556):
		copyT[x] = 0
		copyT[73112 - x] = 0
	py.subplot(4,1,3)
	py.plot(freq,np.absolute(copyT))
	py.title("Frecuencia truncada")
	py.xlabel('Frecuencia(Hz)')
	py.ylabel('Amplitud')
	return copyT

def inversaTruncada(copyT, sound):
	################ Grafico de Frecuencia truncado inversa #######################
	inversa = np.fft.ifft(copyT).real
	py.subplot(4,1,4)
	#py.plot(x,inverseSp)
	py.title("Frecuencia truncada inversa")
	py.xlabel('Tiempo')
	py.ylabel('Amplitud')
	wavfile.write("test.wav",sound[0],inversa)
	return inversa

sound = readFile("handel.wav")
transformada, freq = frecuenciaFourier(sound)
copyT = frecuenciaFourierTruncado(transformada)
inversa = inversaTruncada(copyT,sound)


py.show()