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
	b, a = signal.butter(2, 0.05,'low',analog=True)
	y = signal.filtfilt(b, a, transformada)
	inversa = np.fft.ifft(y).real
	py.plot(y.real)
    py.show()
	wavfile.write("filtradoBajo.wav",sound[0],inversa)


def filtradoAlto(sound):
	transformada = np.fft.fft(sound[1])
	b, a = signal.butter(2, 0.005,'high',analog=True)
	y = signal.filtfilt(b, a, transformada)
	inversa = np.fft.ifft(y).real
	wavfile.write("filtradoAlto.wav",sound[0],inversa)


sound = readFile("handel.wav")

filtradoAlto(sound)
filtradoBajo(sound)
