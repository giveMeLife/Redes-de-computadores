import numpy as np 
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from scipy import interpolate , integrate

def readFile(nombre):
	sound = wavfile.read(nombre)
	return sound

def integral(data,rate):
	integral_array = []
	dataLen = len(data)
	delta = 1/rate
	time = np.linspace(0,(dataLen*1)*delta,dataLen)
	for i  in range(len(data)):
		integral_array.append(integrate.simps(data[:i+1],dx=delta))
	return integral_array

def interpolation(rate,data,time):
	interpol = interpolate.interp1d(time,data)
	time_interpol = np.linspace(0,data.size/rate,data.size*3)
	data_interpol = interpol(time_interpol)
	return data_interpol,time_interpol

def modulationAM(data_interpol,rate,time_interpol,k):
	fc = 3*rate
	coseno = np.cos(2*np.pi*fc*time_interpol)
	result = k * data_interpol * coseno
	return result,coseno

def modulationFM(data_interpol,rate,time_interpol,k):
	##integral = np.cumsum(data_interpol) / rate
	integral_arr = integral(data_interpol,rate)
	fc = 3*rate
	first_term = 2*np.pi*fc*time_interpol
	coseno = np.cos(first_term + k * integral_arr)
	return coseno



rate,data = readFile("handel.wav")
frecuency = data.size / rate
time = np.linspace(0,data.size/rate,data.size)
data_interpol,time_interpol = interpolation(rate,data,time)
data_interpol2,time_interpol2 = interpolation(rate,data,time)
dataAM,portadora = modulationAM(data_interpol,rate,time_interpol,1)
dataFM = modulationFM(data_interpol2,rate,time_interpol2,1)
time_portadora = np.linspace(0,portadora.size/rate,portadora.size)

plt.subplot(4,1,1)
plt.plot(time,data)
plt.subplot(4,1,2)
plt.plot(time_interpol,dataAM)
plt.subplot(4,1,3)
plt.plot(time_portadora,portadora)
plt.subplot(4,1,4)
plt.plot(time_interpol,dataFM)
plt.show()

'''transData = np.fft.fft(data)
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
plt.show()'''


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

