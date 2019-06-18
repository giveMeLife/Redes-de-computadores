import numpy as np 
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from scipy import signal
from scipy import interpolate , integrate

def readFile(nombre):
	sound = wavfile.read(nombre)
	return sound

def interpolation(rate,data):
	time = np.linspace(0,len(data)/rate,len(data))
	interpol = interpolate.interp1d(time,data)
	time_interpol = np.linspace(0,len(data)/rate,len(data))
	data_interpol = interpol(time_interpol)
	return data_interpol

def modulationAM(data,data_interpol,rate,k):
	fc = 3*rate
	time_interpol = np.linspace(0,len(data_interpol)/rate,num=len(data_interpol))
	time = np.linspace(0,len(data)/rate,num=len(data))
	coseno = np.cos(2*np.pi*fc*time_interpol)
	result = k * data_interpol * coseno
	

	return result,coseno

def modulationFM(data,data_interpol,rate,k):
	time_interpol = np.linspace(0,len(data_interpol)/rate,num=len(data_interpol))
	time = np.linspace(0,len(data)/rate,num=len(data))
	integral = np.cumsum(data_interpol) /rate
	fc = 3*rate
	first_term = 2*np.pi*fc*time_interpol
	coseno = np.cos(first_term)
	result = np.cos(first_term + k * integral)
	return result,coseno

def demodulationAM(data_modulation,rate):
	fc = 3*rate
	time_interpol = np.linspace(0,len(data_modulation)/rate,num=len(data_modulation))
	coseno = np.cos(2*np.pi*fc*time_interpol)
	result = data_modulation * coseno
	return result

def filtradoBajo(rate,data):
	b, a = signal.butter(3,4000,'low',fs=rate)
	y = signal.filtfilt(b, a, data)
	transformada2 = np.fft.fft(y).real
	wavfile.write("filtradoBajo.wav",rate,y)
	return y,transformada2

def graphicAM(data,data_interpol,coseno,result):
	time_interpol = np.linspace(0,len(data_interpol)/rate,num=len(data_interpol))
	time = np.linspace(0,len(data)/rate,len(data))
	plt.subplot(3,1,1)
	plt.plot(time,data,'b')
	plt.subplot(3,1,2)
	plt.plot(time_interpol,coseno,'g')
	plt.subplot(3,1,3)
	plt.plot(time_interpol,result,'m')
	plt.show()

def graphicFM(data,data_interpol,coseno,result):
	time_interpol = np.linspace(0,len(data_interpol)/rate,num=len(data_interpol))
	time = np.linspace(0,len(data)/rate,len(data))
	plt.subplot(3,1,1)
	plt.plot(time,data,'b')
	plt.subplot(3,1,2)
	plt.plot(time_interpol,coseno,'g')
	plt.subplot(3,1,3)
	plt.plot(time_interpol,result,'m')
	plt.show()

def graphicFourier(data,rate,color):
	transData = np.fft.fft(data).real
	freq = np.fft.fftfreq(len(data),1/rate)
	plt.plot(freq,transData,color)
	plt.show()

rate,data = readFile("handel.wav")
data_interpol = interpolation(rate,data)
dataAM,portadoraAM = modulationAM(data,data_interpol,rate,1)
dataDemodulationAM = demodulationAM(dataAM,rate)
y,trans = filtradoBajo(rate,dataDemodulationAM)
dataFM,portadoraFM = modulationFM(data,data_interpol,rate,1)
graphicAM(data,data_interpol,portadoraAM,dataAM)
graphicFM(data,data_interpol,portadoraFM,dataFM)

graphicFourier(data,rate,'b')
graphicFourier(dataAM,rate,'m')
graphicFourier(dataFM,rate,'y')
graphicFourier(dataDemodulationAM,rate,'r')

