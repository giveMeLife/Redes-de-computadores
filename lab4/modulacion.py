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
	return result,coseno,fc

def modulationFM(data,data_interpol,rate,k):
	time_interpol = np.linspace(0,len(data_interpol)/rate,num=len(data_interpol))
	time = np.linspace(0,len(data)/rate,num=len(data))
	integral = np.cumsum(data_interpol) /rate
	fc = 3*rate
	first_term = 2*np.pi*fc*time_interpol
	coseno = np.cos(first_term)
	result = np.cos(first_term + k * integral)
	return result,coseno,fc

def demodulationAM(data_modulation,rate):
	fc = 3*rate
	time_interpol = np.linspace(0,len(data_modulation)/rate,num=len(data_modulation))
	coseno = np.cos(2*np.pi*fc*time_interpol)
	result = data_modulation * coseno
	return result

def filtradoBajo(rate,data):
	b, a = signal.butter(3,4000,'low',fs=rate)
	filtered = signal.filtfilt(b, a, data)
	fourier = np.fft.fft(filtered).real
	wavfile.write("filtradoBajo.wav",rate,filtered)
	return filtered,fourier

def graphicAM(data,data_interpol,coseno,result):
	time_interpol = np.linspace(0,len(data_interpol)/rate,num=len(data_interpol))
	time = np.linspace(0,len(data)/rate,len(data))
	fig = plt.figure()
	fig.subplots_adjust(hspace=0.7, wspace=0.7)
	fig.add_subplot(311)
	plt.title("Señal Original")
	plt.xlabel("Tiempo [s]")
	plt.ylabel("Amplitud [dB]")
	plt.plot(time,data,'b')
	fig.add_subplot(312)
	plt.title("Señal Portadora")
	plt.xlabel("Tiempo [s]")
	plt.ylabel("Amplitud [dB]")
	plt.plot(time_interpol,coseno,'g')
	fig.add_subplot(313)
	plt.title("Señal Modulada con AM")
	plt.xlabel("Tiempo [s]")
	plt.ylabel("Amplitud [dB]")
	plt.plot(time_interpol,result,'m')
	plt.show()

def graphicFM(data,data_interpol,coseno,result):
	time_interpol = np.linspace(0,len(data_interpol)/rate,num=len(data_interpol))
	time = np.linspace(0,len(data)/rate,len(data))
	fig = plt.figure()
	fig.subplots_adjust(hspace=0.7, wspace=0.7)
	fig.add_subplot(311)
	plt.title("Señal Original")
	plt.xlabel("Tiempo [s]")
	plt.ylabel("Amplitud [dB]")
	plt.plot(time,data,'b')
	fig.add_subplot(312)
	plt.title("Señal Portadora")
	plt.xlabel("Tiempo [s]")
	plt.ylabel("Amplitud [dB]")
	plt.plot(time_interpol,coseno,'g')
	fig.add_subplot(313)
	plt.title("Señal Modulada con FM")
	plt.xlabel("Tiempo [s]")
	plt.ylabel("Amplitud [dB]")
	plt.plot(time_interpol,result,'m')
	plt.show()

def graphicFourier(data,rate,color,title):
	transData = np.fft.fft(data)
	freq = np.fft.fftfreq(len(data),1/rate)
	plt.title(title)
	plt.xlabel("Frecuencia [Hz]")
	plt.ylabel("Amplitud [dB]")
	plt.plot(freq,abs(transData),color)
	plt.show()

rate,data = readFile("handel.wav")
data_interpol = interpolation(rate,data)

####################### MODULACION 100%#######################################
dataAM_1,portadoraAM_1,rateAM_1 = modulationAM(data,data_interpol,rate,1)
dataDemodulationAM_1 = demodulationAM(dataAM_1,rate)
filtered_1,trans_1 = filtradoBajo(rate,dataDemodulationAM_1)
dataFM_1,portadoraFM_1,rateFM_1 = modulationFM(data,data_interpol,rate,1)
graphicAM(data,data_interpol,portadoraAM_1,dataAM_1)
graphicFM(data,data_interpol,portadoraFM_1,dataFM_1)

graphicFourier(data,rate,'b',"Transformada de Fourier señal original")
graphicFourier(dataAM_1,rateAM_1,'m',"Transformada de Fourier con modulacion AM")
graphicFourier(dataFM_1,rateFM_1,'y',"Transformada de Fourier con modulacion FM")
graphicFourier(dataDemodulationAM_1,rate,'r',"Transformada de Fourier señal demodulada")

####################### MODULACION 15%#######################################
dataAM_15,portadoraAM_15,rateAM_15 = modulationAM(data,data_interpol,rate,0.15)
dataDemodulationAM_15 = demodulationAM(dataAM_15,rate)
filtered_15,trans_15 = filtradoBajo(rate,dataDemodulationAM_15)
dataFM_15,portadoraFM_15,rateFM_15 = modulationFM(data,data_interpol,rate,0.15)
graphicAM(data,data_interpol,portadoraAM_15,dataAM_15)
graphicFM(data,data_interpol,portadoraFM_15,dataFM_15)

graphicFourier(data,rate,'b',"Transformada de Fourier señal original")
graphicFourier(dataAM_15,rateAM_15,'m',"Transformada de Fourier con modulacion AM")
graphicFourier(dataFM_15,rateFM_15,'y',"Transformada de Fourier con modulacion FM")
graphicFourier(dataDemodulationAM_15,rate,'r',"Transformada de Fourier señal demodulada")

####################### MODULACION 125%#######################################
dataAM_125,portadoraAM_125,rateAM_125 = modulationAM(data,data_interpol,rate,1.25)
dataDemodulationAM_125 = demodulationAM(dataAM_125,rate)
filtered_125,trans_125 = filtradoBajo(rate,dataDemodulationAM_125)
dataFM_125,portadoraFM_125,rateFM_125 = modulationFM(data,data_interpol,rate,1.25)
graphicAM(data,data_interpol,portadoraAM_125,dataAM_125)
graphicFM(data,data_interpol,portadoraFM_125,dataFM_125)

graphicFourier(data,rate,'b',"Transformada de Fourier señal original")
graphicFourier(dataAM_125,rateAM_125,'m',"Transformada de Fourier con modulacion AM")
graphicFourier(dataFM_125,rateFM_125,'y',"Transformada de Fourier con modulacion FM")
graphicFourier(dataDemodulationAM_125,rate,'r',"Transformada de Fourier señal demodulada")