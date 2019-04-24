import numpy as np 
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from scipy import signal

def readFile(nombre):
	sound = wavfile.read(nombre)
	return sound

sound = readFile("handel.wav")
freq, time, espec = signal.spectrogram(sound[1],sound[0])
plt.pcolormesh(time,freq,espec)
plt.ylabel("Frecuencia")
plt.xlabel("Tiempo")
plt.show()