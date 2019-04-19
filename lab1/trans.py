import numpy as np
import matplotlib.pyplot as py
import scipy.io.wavfile as wavfile
from scipy.fftpack import fft

#Descripción: Función que permite leer un archivo de sonido .wav en el directorio del programa
#Entradas: Un string que es el nombre del archivo a leer
#Salida: Un arreglo donde su primer elemento es la cantidad de muestras obtenidas en un segundo
#		 y el segundo elemento es un arreglo con el total de muestras obtenidas del archivo.
def readFile(nombre):
	sound = wavfile.read(nombre)
	return sound

#Gráfico de amplitud v/s tiempo
#Descripción: Función que grafica una muestra de amplitudes de un sonido en el tiempo
#Entrada: Un arreglo donde su primer elemento es la cantidad de muestras obtenidas en un segundo
#  		  y el segundo elemento es un arreglo con el total de muestras obtenidas del archivo.
#Salida: 
def graficoTiempo(sound):
	x = np.linspace(0,sound[1].size/sound[0],sound[1].size)
	y=sound[1]
	'''py.figure(1)
	py.plot(x,y,'b')
	py.title("Amplitud v/s Tiempo")
	py.xlabel("Tiempo (s)")
	py.ylabel("Amplitud")
	py.title("Funcion en el Tiempo original")'''

#Grafico Transformada Fourier 
#Descripción: Función que realiza una transformada de Fourier un set de datos correspondientes a la amplitud de un sonido
#             , calcula la frecuencia sobre la que se proyectan y genera el gráfico
#Entrada: Un arreglo donde su primer elemento es la cantidad de muestras obtenidas en un segundo
#  		  y el segundo elemento es un arreglo con el total de muestras obtenidas del archivo.
#Salida: Un arreglo con la transformada de Fourier de las muestras de un sonido y otro arreglo con
#		 la frecuencia sobre la que se proyectan
def frecuenciaFourier(sound):
	transformada = np.fft.fft(sound[1])
	freq = np.fft.fftfreq(sound[1].size,1/sound[0])
	'''py.figure(2)
	py.plot(freq,np.absolute(transformada),'g')
	py.title("Amplitud v/s Frecuencia")
	py.xlabel('Frecuencia')
	py.ylabel('Amplitud')
	#py.show()'''
	return transformada,freq

#Transformada de Fourier truncada
#Descripción: Función que trunca ciertos valores de una transformada de Fourier a 0.
#Entrada: Un arreglo con los datos obtenidos al realizar la transformada de Fourier del sonido
#Salida: Arreglo con datos truncados a 0 del arreglo de entrada.
def frecuenciaFourierTruncado(transformada):
	copyT = transformada.copy()
	freq = np.fft.fftfreq(sound[1].size,1/sound[0])
	for x in range(2000):
		copyT[x] = 0
		copyT[73112 - x] = 0
	for x in range(12000,36556):
		copyT[x] = 0
		copyT[73112 - x] = 0
	'''py.figure(3)
	py.plot(freq,np.absolute(copyT),'m')
	py.title("Transformada De Fourier truncada")
	py.xlabel('Frecuencia(Hz)')
	py.ylabel('Amplitud')
	#py.show()'''
	return copyT

#Gráfico transformada de Fourier inversa truncada y genera un archivo de sonido nuevo
#Descripción: Función que obtiene la transformada de Fourier inversa de un arreglo de datos
#Entrada: Un arreglo con un set de datos correspondiente a la transformada de Fourier truncada y
# 		  un arreglo donde su primer elemento es la cantidad de muestras obtenidas en un segundo
#  		  y el segundo elemento es un arreglo con el total de muestras obtenidas del archivo.
#Salida: Un arreglo con los valores de la transformada de Fourier inversa truncada

def inversaTruncada(copyT, sound):
	inversa = np.fft.ifft(copyT).real
	x = np.linspace(0,sound[1].size/sound[0],sound[1].size)
	'''py.figure(4)
	py.plot(x,inversa,'r')
	py.title("Transformada inversa de Fourier truncada")
	py.xlabel('Tiempo')
	py.ylabel('Amplitud')
	py.show()'''
	wavfile.write("test.wav",sound[0],inversa)
	return inversa

#Descripción: Función que calcula el error cuadrático medio entre dos arreglos
#Entrada: Dos arreglos con datos de largo 73113
#salida: Error cuadrático medio de los dos arreglos.
def errorCuadratico(real,calculado):
	sumatoria = 0
	for x in range(73113):
		sumatoria = sumatoria + (calculado[x]-real[x])**2
	print(sumatoria)
	div = sumatoria / 73113.0
	raiz = np.sqrt(div)
	return raiz


#################################BLOQUE PRINCIPAL#######################################
sound = readFile("handel.wav")
graficoTiempo(sound)
transformada, freq = frecuenciaFourier(sound)
copyT = frecuenciaFourierTruncado(transformada)
inversa = np.fft.ifft(transformada).real
inversaTruncada = inversaTruncada(copyT,sound)
errorNormalInversaTruncada = errorCuadratico(sound[1],inversaTruncada)
errorNormalInversa = errorCuadratico(sound[1],inversa)

print("El error cuadrático medio entre la muestra inicial, y la transformada inversa truncada es: ",errorNormalInversaTruncada)

print("El error cuadrático medio entre la muestra inicial, y la transformada inversa es: ",errorNormalInversa)

