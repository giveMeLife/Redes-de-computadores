import numpy as np
import matplotlib.pyplot as py
import scipy.io.wavfile as wavfile
from scipy.fftpack import fft

############### Grafico de Tiempo ############################
def readFile(nombre):
	sound = wavfile.read(nombre)
	return sound

def graficoTiempo(sound):
	x = np.linspace(0,sound[1].size/sound[0],sound[1].size)
	y=sound[1]
	py.figure(1)
	py.plot(x,y)
	py.xlabel("Tiempo (s)")
	py.ylabel("Amplitud")
	py.title("Funcion en el Tiempo original")

################ Grafico de Frecuencia #######################
def frecuenciaFourier(sound):
	transformada = np.fft.fft(sound[1])
	freq = np.fft.fftfreq(sound[1].size,1/sound[0])
	py.figure(2)
	py.plot(freq,np.absolute(transformada))
	py.xlabel('Frecuencia')
	py.ylabel('Amplitud')
	#py.show()
	return transformada,freq

################ Grafico de Frecuencia truncado #######################
def frecuenciaFourierTruncado(transformada):
	copyT = transformada.copy()
	for x in range(2000):
		copyT[x] = 0
		copyT[73112 - x] = 0
	for x in range(12000,36556):
		copyT[x] = 0
		copyT[73112 - x] = 0
	#py.subplot(4,1,3)
	py.figure(3)
	py.plot(freq,np.absolute(copyT))
	py.title("Frecuencia truncada")
	py.xlabel('Frecuencia(Hz)')
	py.ylabel('Amplitud')
	#py.show()
	return copyT

################ Grafico de Frecuencia truncado inversa #######################
def inversaTruncada(copyT, sound):
	inversa = np.fft.ifft(copyT).real
	x = np.linspace(0,sound[1].size/sound[0],sound[1].size)
	py.figure(4)
	py.plot(x,inversa)
	py.title("Frecuencia truncada inversa")
	py.xlabel('Tiempo')
	py.ylabel('Amplitud')
	py.show()
	wavfile.write("test.wav",sound[0],inversa)
	return inversa


def errorCuadtratico(real,calculado):
	sumatoria = 0
	for x in range(73113):
		sumatoria = sumatoria + (calculado[x]-real[x])**2
	print(sumatoria)
	div = sumatoria / 73113.0
	raiz = np.sqrt(div)
	return raiz


sound = readFile("handel.wav")
graficoTiempo(sound)
transformada, freq = frecuenciaFourier(sound)
copyT = frecuenciaFourierTruncado(transformada)
inversa = inversaTruncada(copyT,sound)
error = errorCuadtratico(sound[1],inversa)

print(error)
