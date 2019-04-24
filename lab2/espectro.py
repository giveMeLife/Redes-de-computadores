import numpy as np 
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from scipy import signal

def readFile(nombre):
	sound = wavfile.read(nombre)
	return sound

sound = readFile("handel.wav")
freq, time, espec = signal.spectrogram(sound[1],sound[0])
test = np.log10(espec)
im = plt.pcolormesh(time,freq,test)
plt.ylabel("Frecuencia [Hz]")
plt.xlabel("Tiempo [s]")
plt.colorbar(im).set_label('Intensidad [dB]')
plt.show()