import numpy as np 
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from scipy import interpolate

def readFile(nombre):
	sound = wavfile.read(nombre)
	return sound

def interpolation(frecuency,data,time):
	interpol = interpolate.interp1d(time,data)
	time_interpol = np.linspace(0,frecuency,data.size*3)
	data_interpol = interpol(time_interpol)
	return data_interpol,time_interpol

def modulationAM(data_interpol,frecuency,time_interpol,k):
	coseno = np.cos(2*np.pi*frecuency*time_interpol)
	result = k * data_interpol * coseno
	return result

def modulationFM(data_interpol,frecuency,time_interpol,k):
	integral = np.cumsum(data_interpol)
	first_term = 2*np.pi*frecuency*time_interpol
	coseno = np.cos(first_term + k * integral)
	return coseno



rate,data = readFile("handel.wav")
frecuency = data.size / rate
time = np.linspace(0,frecuency,data.size)
data_interpol,time_interpol = interpolation(frecuency,data,time)
dataAM = modulationAM(data_interpol,frecuency,time_interpol,1)
dataFM = modulationFM(data_interpol,frecuency,time_interpol,1)

plt.subplot(3,1,1)
plt.plot(time,data)
plt.subplot(3,1,2)
plt.plot(time_interpol,dataAM)
plt.subplot(3,1,3)
plt.plot(time_interpol,dataFM)
plt.show()

transData = np.fft.fft(data)
freq = np.fft.fftfreq(data.size,1/rate)
transDataAM = np.fft.fft(dataAM)
freqAM = np.fft.fftfreq(dataAM.size,1/rate)
transDataFM = np.fft.fft(dataFM)
freqFM = np.fft.fftfreq(dataFM.size,1/rate)

plt.subplot(3,1,1)
plt.plot(freq,transData)
plt.subplot(3,1,2)
plt.plot(freqAM,transDataAM)
plt.subplot(3,1,3)
plt.plot(freqFM,transDataFM)
plt.show()


'''interpolada = interpolate.interp1d(time,sound[1])
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
cosenoFM = np.cos(2*np.pi*frecuencia*time_interpolada + integral)'''

