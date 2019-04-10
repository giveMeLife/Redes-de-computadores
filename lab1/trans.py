import numpy as np
import matplotlib.pyplot as py
import scipy.io.wavfile as wavfile
from scipy.fftpack import fft

sound = wavfile.read("handel.wav")
sp = np.fft.fft(sound[1])
freq = np.fft.fftfreq(sound[1].size,1/sound[0])
py.plot(freq,sp)
py.xlabel('Frecuencia(Hz)')
py.ylabel('Amplitud')
py.show()