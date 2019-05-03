import numpy as np
import matplotlib.pyplot as py
import scipy.io.wavfile as wavfile
from scipy import signal
from scipy.fftpack import fft

#Descripción: Función que permite leer un archivo de sonido .wav en el directorio del programa
#Entradas: Un string que es el nombre del archivo a leer
#Salida: Un arreglo donde su primer elemento es la cantidad de muestras obtenidas en un segundo
#		 y el segundo elemento es un arreglo con el total de muestras obtenidas del archivo.
def readFile(nombre):
	sound = wavfile.read(nombre)
	return sound

#Descripción: Función que permite obtener la transformada de Fourier para la señal original
#Entradas: Arreglo con los datos del audio.
#Salida: Transformada de Fourier de la Función.
def datosFuncionNormal(sound):
	transformada = np.fft.fft(sound[1])
	return transformada

#Descripción: Función que aplica el filtrado bajo a los datos del audio original.
#Entradas: Arreglo con los datos del audio original
#Salida: Datos de la Funcion a los que se le aplicó el filtrado bajo y el segundo parametro es 
#		la transformada de Fourier de estos datos. 
def filtradoBajo(sound):
	transformada = np.fft.fft(sound[1])
	b, a = signal.butter(3, 2000,'low',fs=sound[0])
	y = signal.filtfilt(b, a, sound[1])
	transformada2 = np.fft.fft(y).real
	wavfile.write("filtradoBajo.wav",sound[0],y)
	return y,transformada2

#Descripción: Función que aplica el filtrado alto a los datos del audio original.
#Entradas: Arreglo con los datos del audio original
#Salida: Datos de la Funcion a los que se le aplicó el filtrado alto y el segundo parametro es 
#		la transformada de Fourier de estos datos. 
def filtradoAlto(sound):
	transformada = np.fft.fft(sound[1])
	b, a = signal.butter(3, 500,'high',fs=sound[0])
	y = signal.filtfilt(b, a, sound[1])
	transfromada2 = np.fft.fft(y).real
	wavfile.write("filtradoAlto.wav",sound[0],y)
	return y,transfromada2

#Descripción: Función que aplica el filtrado banda a los datos del audio original.
#Entradas: Arreglo con los datos del audio original
#Salida: Datos de la Funcion a los que se le aplicó el filtrado banda y el segundo parametro es 
#		la transformada de Fourier de estos datos. 
def filtradoBanda(sound):
	transformada = np.fft.fft(sound[1])
	b, a = signal.butter(5, [2000,3000],'band',fs=sound[0])
	y = signal.filtfilt(b, a, sound[1])
	transformada2 = np.fft.fft(y).real
	wavfile.write("filtradoBanda.wav",sound[0],y)
	return y,transformada2

#Descripción: Función que grafica la amplitud versus el tiempo para los datos obtenidos con
#			las funciones filtradoAlto, filtradoBajo y filtradoBanda, ademas de los datos originales del audio.
#Entradas: Arreglo con la duracion del audio, datos del audio original, datos del filtrado alto, datos del filtrado bajo
#			y datos del filtrado banda.
#Salida:
def graficosTiempo(x,sound,filtAlto,filtBajo,filtBanda):
	fig3 = py.figure()
	fig3.subplots_adjust(hspace=0.7, wspace=0.7)
	fig3.add_subplot(221)
	py.title("Funcion Normal")
	py.xlabel("Tiempo [s]")
	py.ylabel("Amplitud [dB]")
	py.plot(x,sound[1],'y')
	fig3.add_subplot(222)
	py.title("Funcion con Filtro Alto")
	py.xlabel("Tiempo [s]")
	py.ylabel("Amplitud [dB]")
	py.plot(x,filtAlto,'g')
	fig3.add_subplot(223)
	py.title("Funcion con Filtro Bajo")
	py.xlabel("Tiempo [s]")
	py.ylabel("Amplitud [dB]")
	py.plot(x,filtBajo,'r')
	fig3.add_subplot(224)
	py.title("Funcion con Filtro Banda")
	py.plot(x,filtBanda)
	py.xlabel("Tiempo [s]")
	py.ylabel("Amplitud [dB]")

#Descripción: Función que grafica la amplitud versus la frecuencia para los datos obtenidos con las funciones
#			 datosFuncionNormal, filtradoAlto, filtradoBajo y filtradoNormal.
#Entradas: frecuencias del audio, arreglo de datos de la transformada de Fourier de la funcion original y arreglo de datos 
#			de la transformada de Fourier para los obtenidos con los filtros alto, bajo y banda
#Salida: 
def graficosFrecuencia(freq, transNormal,transBajo,transBanda,transAlto):
	fig = py.figure()
	fig.subplots_adjust(hspace=0.7, wspace=0.7)
	fig.add_subplot(221)
	py.title("Frecuencia con Filtro Alto")
	py.xlabel("Frecuencia [Hz]")
	py.ylabel("Amplitud [dB]")
	py.plot(freq,abs(transNormal),'y')
	fig.add_subplot(222)
	py.title("Frecuencia con Filtro Alto")
	py.xlabel("Frecuencia [Hz]")
	py.ylabel("Amplitud [dB]")
	py.plot(freq,abs(transAlto),'g')
	fig.add_subplot(223)
	py.title("Frecuencia con Filtro Bajo")
	py.xlabel("Frecuencia [Hz]")
	py.ylabel("Amplitud [dB]")
	py.plot(freq,abs(transBajo),'r')
	fig.add_subplot(224)
	py.title("Frecuencia con Filtro Banda")
	py.plot(freq,abs(transBanda))
	py.xlabel("Frecuencia [Hz]")
	py.ylabel("Amplitud [dB]")

#Descripción: Crea el espectograma para la funcion original y los datos del filtro alto, banda y bajo.
#Entrada: Datos de la funcion original, datos del filtrado alto, datos del filtrado bajo y datos
#		datos del filtrado banda
#Salida:
def espectograma(sound,filtAlto,filtBajo,filtBanda):
	fig2 = py.figure()
	fig2.subplots_adjust(hspace=0.5, wspace=0.5)
	fig2.add_subplot(221)
	freqNormal, timeNormal, especNormal = signal.spectrogram(sound[1],sound[0])
	testNormal = np.log10(especNormal)
	imNormal = py.pcolormesh(timeNormal,freqNormal,testNormal)
	py.colorbar(imNormal).set_label('Amplitud [dB]')
	py.title("Espectrograma funcion sin filtro")
	py.ylabel("Frecuencia [Hz]")
	py.xlabel("Tiempo [s]")
	fig2.add_subplot(222)
	freqAlto, timeAlto, especAlto = signal.spectrogram(filtAlto.real,sound[0])
	testAlto = np.log10(especAlto)
	imAlto = py.pcolormesh(timeAlto,freqAlto,testAlto)
	py.colorbar(imAlto).set_label('Amplitud [dB]')
	py.title("Espectrograma funcion con filtro alto")
	py.ylabel("Frecuencia [Hz]")
	py.xlabel("Tiempo [s]")
	fig2.add_subplot(223)
	freqBajo, timeBajo, especBajo = signal.spectrogram(filtBajo.real,sound[0])
	testBajo = np.log10(especBajo)
	imBajo = py.pcolormesh(timeBajo,freqBajo,testBajo)
	py.colorbar(imBajo).set_label('Amplitud [dB]')
	py.title("Espectrograma funcion con filtro bajo")
	py.ylabel("Frecuencia [Hz]")
	py.xlabel("Tiempo [s]")
	fig2.add_subplot(224)
	freqBanda, timeBanda, especBanda = signal.spectrogram(filtBanda.real,sound[0])
	testBanda = np.log10(especBanda)
	imBanda = py.pcolormesh(timeBanda,freqBanda,testBanda)
	py.title("Espectrograma funcion con filtro banda")
	py.ylabel("Frecuencia [Hz]")
	py.xlabel("Tiempo [s]")
	py.colorbar(imBanda).set_label('Amplitud [dB]')


######################Bloque Principal#########################################
sound = readFile("handel.wav")

x = np.linspace(0,sound[1].size/sound[0],sound[1].size)
freq = np.fft.fftfreq(sound[1].size,1/sound[0])
transNormal = datosFuncionNormal(sound)
filtAlto, transAlto = filtradoAlto(sound)
filtBajo, transBajo = filtradoBajo(sound)
filtBanda, transBanda = filtradoBanda(sound)

graficosTiempo(x,sound,filtAlto,filtBajo,filtBanda)
graficosFrecuencia(freq, transNormal,transBajo,transBanda,transAlto)
espectograma(sound,filtAlto,filtBajo,filtBanda)
py.show()