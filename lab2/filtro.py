import numpy as np
import matplotlib.pyplot as py
import scipy.io.wavfile as wavfile
from scipy import signal
from scipy.fftpack import fft


def readFile(nombre):
	sound = wavfile.read(nombre)
	return sound


sound = readFile("handel.wav")
transformada = np.fft.fft(sound[1])
b, a = signal.butter(4, 100,'low',analog=True)
y = signal.filtfilt(b, a, transformada)
inversa = np.fft.ifft(transformada).real
wavfile.write("filtrado.wav",sound[0],inversa)

