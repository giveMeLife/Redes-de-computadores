import numpy as np
import matplotlib.pyplot as py
import scipy.io.wavfile as wavfile
from scipy import signal
from scipy.fftpack import fft


def readFile(nombre):
	sound = wavfile.read(nombre)
	return sound

def filtradoBajo(sound):
	transformada = np.fft.fft(sound[1])
	b, a = signal.butter(3, 2000,'low',fs=sound[0])
	freq = np.fft.fftfreq(sound[1].size,1/sound[0])
	y = signal.filtfilt(b, a, sound[1])
	transformada2 = np.fft.fft(y).real
	#freq2, time, espec = signal.spectrogram(y.real,sound[0])
	#test = np.log10(espec)
	#im = py.pcolormesh(time,freq2,test)
	#py.plot(freq,abs(inversa))
	#py.show()
	wavfile.write("filtradoBajo.wav",sound[0],y)
	return y,transformada2


def filtradoAlto(sound):
	transformada = np.fft.fft(sound[1])
	b, a = signal.butter(3, 3000,'high',fs=sound[0])
	y = signal.filtfilt(b, a, sound[1])
	freq = np.fft.fftfreq(sound[1].size,1/sound[0])
	transfromada2 = np.fft.fft(y).real
	#freq2, time, espec = signal.spectrogram(y.real,sound[0])
	#test = np.log10(espec)
	#im = py.pcolormesh(time,freq2,test)
	#py.show()
	#py.plot(freq,abs(inversa))
	#py.show()
	wavfile.write("filtradoAlto.wav",sound[0],y)
	return y,transfromada2

def filtradoBanda(sound):
	transformada = np.fft.fft(sound[1])
	b, a = signal.butter(5, [2000,3000],'band',fs=sound[0])
	y = signal.filtfilt(b, a, sound[1])
	freq = np.fft.fftfreq(sound[1].size,1/sound[0])
	transformada2 = np.fft.fft(y).real
	#freq2, time, espec = signal.spectrogram(y,sound[0])
	#test = np.log10(espec)
	#im = py.pcolormesh(time,freq2,test)
	#py.colorbar(im).set_label('Intensidad [dB]')
	#py.plot(freq,abs(inversa))
	#py.show()
	wavfile.write("filtradoBanda.wav",sound[0],y)
	return y,transformada2


sound = readFile("handel.wav")

freq = np.fft.fftfreq(sound[1].size,1/sound[0])
filtAlto, transAlto = filtradoAlto(sound)
filtBajo, transBajo = filtradoBajo(sound)
filtBanda, transBanda = filtradoBanda(sound)

'''fig = py.figure()
fig.subplots_adjust(hspace=0.7, wspace=0.7)
fig.add_subplot(311)
py.title("Frecuencia con Filtro Alto")
py.xlabel("Frecuencia [Hz]")
py.ylabel("Amplitud")
py.plot(freq,abs(transAlto),'g')
fig.add_subplot(312)
py.title("Frecuencia con Filtro Bajo")
py.xlabel("Frecuencia [Hz]")
py.ylabel("Amplitud")
py.plot(freq,abs(transBajo),'r')
fig.add_subplot(313)
py.title("Frecuencia con Filtro Banda")
py.plot(freq,abs(transBanda))
py.xlabel("Frecuencia [Hz]")
py.ylabel("Amplitud")
py.show()'''


fig2 = py.figure()
fig2.subplots_adjust(hspace=0.7, wspace=0.7)
fig2.add_subplot(311)
freqAlto, timeAlto, especAlto = signal.spectrogram(filtAlto.real,sound[0])
testAlto = np.log10(especAlto)
imAlto = py.pcolormesh(timeAlto,freqAlto,testAlto)
fig2.add_subplot(312)
py.title("Frecuencia con Filtro Bajo")
py.xlabel("Frecuencia [Hz]")
py.ylabel("Amplitud")
py.plot(freq,abs(transBajo),'r')
fig2.add_subplot(313)
py.title("Frecuencia con Filtro Banda")
py.plot(freq,abs(transBanda))
py.xlabel("Frecuencia [Hz]")
py.ylabel("Amplitud")
py.show()