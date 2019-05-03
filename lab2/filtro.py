import numpy as np
import matplotlib.pyplot as py
import scipy.io.wavfile as wavfile
from scipy import signal
from scipy.fftpack import fft


def readFile(nombre):
	sound = wavfile.read(nombre)
	return sound

def datosFuncionNormal(sound):
	transformada = np.fft.fft(sound[1])
	return transformada

def filtradoBajo(sound):
	transformada = np.fft.fft(sound[1])
	b, a = signal.butter(3, 2000,'low',fs=sound[0])
	y = signal.filtfilt(b, a, sound[1])
	transformada2 = np.fft.fft(y).real
	wavfile.write("filtradoBajo.wav",sound[0],y)
	return y,transformada2

def filtradoAlto(sound):
	transformada = np.fft.fft(sound[1])
	b, a = signal.butter(3, 2000,'high',fs=sound[0])
	y = signal.filtfilt(b, a, sound[1])
	transfromada2 = np.fft.fft(y).real
	wavfile.write("filtradoAlto.wav",sound[0],y)
	return y,transfromada2

def filtradoBanda(sound):
	transformada = np.fft.fft(sound[1])
	b, a = signal.butter(5, [2000,3000],'band',fs=sound[0])
	y = signal.filtfilt(b, a, sound[1])
	transformada2 = np.fft.fft(y).real
	wavfile.write("filtradoBanda.wav",sound[0],y)
	return y,transformada2

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

def espectograma(sound,filtAlto,filtBajo,filtBanda):
	fig2 = py.figure()
	fig2.subplots_adjust(hspace=0.5, wspace=0.5)
	fig2.add_subplot(221)
	freqNormal, timeNormal, especNormal = signal.spectrogram(sound[1],sound[0])
	testNormal = np.log10(especNormal)
	imNormal = py.pcolormesh(timeNormal,freqNormal,testNormal)
	py.colorbar(imNormal).set_label('Intensidad [dB]')
	py.title("Espectograma funcion sin filtro")
	py.ylabel("Frecuencia [Hz]")
	py.xlabel("Tiempo [s]")
	fig2.add_subplot(222)
	freqAlto, timeAlto, especAlto = signal.spectrogram(filtAlto.real,sound[0])
	testAlto = np.log10(especAlto)
	imAlto = py.pcolormesh(timeAlto,freqAlto,testAlto)
	py.colorbar(imAlto).set_label('Intensidad [dB]')
	py.title("Espectograma funcion con filtro alto")
	py.ylabel("Frecuencia [Hz]")
	py.xlabel("Tiempo [s]")
	fig2.add_subplot(223)
	freqBajo, timeBajo, especBajo = signal.spectrogram(filtBajo.real,sound[0])
	testBajo = np.log10(especBajo)
	imBajo = py.pcolormesh(timeBajo,freqBajo,testBajo)
	py.colorbar(imBajo).set_label('Intensidad [dB]')
	py.title("Espectograma funcion con filtro bajo")
	py.ylabel("Frecuencia [Hz]")
	py.xlabel("Tiempo [s]")
	fig2.add_subplot(224)
	freqBanda, timeBanda, especBanda = signal.spectrogram(filtBanda.real,sound[0])
	testBanda = np.log10(especBanda)
	imBanda = py.pcolormesh(timeBanda,freqBanda,testBanda)
	py.title("Espectograma funcion con filtro banda")
	py.ylabel("Frecuencia [Hz]")
	py.xlabel("Tiempo [s]")
	py.colorbar(imBanda).set_label('Intensidad [dB]')

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