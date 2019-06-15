import numpy as np 
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from scipy import interpolate

def readFile(nombre):
	sound = wavfile.read(nombre)
	return sound

sound = readFile("handel.wav")
time = np.linspace(0,sound[1].size/sound[0],sound[1].size)
interpolada = interpolate.interp1d(time,sound[1])
time2 = np.linspace(0,sound[1].size/sound[0],sound[1].size*3)
sound2 = interpolada(time2)
frecuencia = sound[1].size/sound[0]
time_interpolada = np.linspace(0,sound2.size/sound[0],sound2.size)

###########Modulacion AM########################
coseno = np.cos(2*np.pi*frecuencia*time_interpolada)
result = sound2 * coseno
#################################################

#integral = np.cumsum(sound2) / frecuencia

###########Modulacion FM#########################
integral = np.cumsum(sound2)
cosenoFM = np.cos(2*np.pi*frecuencia*time_interpolada + integral)

