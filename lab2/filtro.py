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
	inversa = np.fft.fft(y).real
	py.plot(freq,abs(inversa))
	py.show()
	wavfile.write("filtradoBajo.wav",sound[0],inversa)


def filtradoAlto(sound):
	transformada = np.fft.fft(sound[1])
	b, a = signal.butter(2, 2000,'high',fs=sound[0])
	y = signal.filtfilt(b, a, sound[1])
	freq = np.fft.fftfreq(sound[1].size,1/sound[0])
	inversa = np.fft.ifft(y).real
	py.plot(freq,abs(inversa))
	py.show()
	wavfile.write("filtradoAlto.wav",sound[0],inversa)

def filtradoBanda(sound):
	transformada = np.fft.fft(sound[1])
	b, a = signal.butter(2, [1000,4000],'band',fs=sound[0])
	y = signal.filtfilt(b, a, sound[1])
	freq = np.fft.fftfreq(sound[1].size,1/sound[0])
	inversa = np.fft.ifft(y).real
	py.plot(freq,abs(inversa))
	py.show()
	wavfile.write("filtradoBanda.wav",sound[0],inversa)



sound = readFile("handel.wav")

filtradoAlto(sound)
filtradoBajo(sound)
filtradoBanda(sound)

