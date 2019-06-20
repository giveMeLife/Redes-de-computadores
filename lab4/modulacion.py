import numpy as np 
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from scipy import signal
from scipy import interpolate , integrate

#Entrada: Nombre del archivo 
#Proceso: Lee la informacion del archivo de audio. 
#Salida: Un arreglo con dos elementos, el primero es la cantidad de datos en un segundo y el otro es la informacion del audio.
def readFile(name):
	sound = wavfile.read(name)
	return sound

#Entrada: Cantidad de datos en un segundo y la informacion del audio original.
#Proceso: Realiza la interpolacion a los datos ingresados.
#Salida: La nueva informacion sobre la señal interpolada.
def interpolation(rate,data):
	time = np.linspace(0,len(data)/rate,len(data))
	interpol = interpolate.interp1d(time,data)
	time_interpol = np.linspace(0,len(data)/rate,len(data))
	data_interpol = interpol(time_interpol)
	return data_interpol

#Entrada: data_interpol es la informacion de la señal interpolada, rate la cantidad de elementos en un segundo y k es el porcentaje que se aplica. 
#Proceso: Realiza la modulacion AM. Calcula una nueva frecuencia y es ingresada junto a data_interpol en un coseno para crear la señal portadora, 
# 		  la cual es multiplicado por K y los datos de la señal modulada.
#Salida: El resultado de la modulacion, la señal portadora y la frecuencia de muestreo.
def modulationAM(data_interpol,rate,k):
	fc = 3*rate
	time_interpol = np.linspace(0,len(data_interpol)/rate,num=len(data_interpol))
	coseno = np.cos(2*np.pi*fc*time_interpol)
	result = k * data_interpol * coseno
	return result,coseno,fc

#Entrada: data_interpol es la informacion de la señal interpolada, rate la cantidad de elementos en un segundo y k el porcentaje que se aplica.
#Proceso: Realiza la modulacion FM. Calcula la integral aproximada de la señal en cada punto, crea una frecuencia de muestreo y calcula el primer termino del coseno.
#		  Todos estos parametros son ingresados a un coseno que es la señal portadora. 
#Salida: Retorna el resultado de la modulacion, la señal portadora y la frecuencia de muestreo.
def modulationFM(data_interpol,rate,k):
	time_interpol = np.linspace(0,len(data_interpol)/rate,num=len(data_interpol))
	integral = np.cumsum(data_interpol) /rate
	fc = 3*rate
	first_term = 2*np.pi*fc*time_interpol
	coseno = np.cos(first_term)
	result = np.cos(first_term + k * integral)
	return result,coseno,fc

#Entrada: data_modulation es la informacion de la señal modulada, rate es la cantidad de elementos en un segundo, ademas del porcentaje.
#Proceso: Calcula una nueva portadora (un coseno) y lo multiplica con los datos de la modulacion AM.
#Return: La señal despues de la demodulacion.
def demodulationAM(data_modulation,rate,k):
	fc = 3*rate
	time_interpol = np.linspace(0,len(data_modulation)/rate,num=len(data_modulation))
	coseno = np.cos(2*np.pi*fc*time_interpol)
	result = k * data_modulation * coseno
	return result

#Entrada: Cantidad de datos en un segundo, informacion de la señal demodulada.
#Proceso: Elimina las frecuencias altas de la señal demodulada.
#Salida: La señal filtrada por un pasa bajo.
def filtradoBajo(rate,data):
	b, a = signal.butter(3,4000,'low',fs=rate)
	filtered = signal.filtfilt(b, a, data)
	wavfile.write("filtradoBajo.wav",rate,filtered)
	return filtered

#Entrada: data es la informacion de la señal original, data_interpol es la informacion de la señal interpolada, coseno es la portadora, 
#		  result es la señal modulada y percentage es el porcentaje aplicado.
#Process: Grafica la señal original, la portadora y la señal modulada.
def graphicAM(data,data_interpol,coseno,result,percentage):
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
	plt.title("Señal Portadora con "+ percentage)
	plt.xlabel("Tiempo [s]")
	plt.ylabel("Amplitud [dB]")
	plt.plot(time_interpol,coseno,'g')
	fig.add_subplot(313)
	plt.title("Señal Modulada con AM al "+ percentage)
	plt.xlabel("Tiempo [s]")
	plt.ylabel("Amplitud [dB]")
	plt.plot(time_interpol,result,'m')
	plt.show()

#Entrada: data es la informacion de la señal original, data_interpol es la informacion de la señal interpolada, coseno es la portadora, 
#		  result es la señal modulada y percentage es el porcentaje aplicado.
#Proceso: Grafica la señal original, la portadora y la señal modulada.
def graphicFM(data,data_interpol,coseno,result,percentage):
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
	plt.title("Señal Portadora con "+ percentage)
	plt.xlabel("Tiempo [s]")
	plt.ylabel("Amplitud [dB]")
	plt.plot(time_interpol,coseno,'g')
	fig.add_subplot(313)
	plt.title("Señal Modulada con FM  al "+ percentage)
	plt.xlabel("Tiempo [s]")
	plt.ylabel("Amplitud [dB]")
	plt.plot(time_interpol,result,'m')
	plt.show()

#Entrada: Recibe la informacion de la señal y la cantidad de elementos por segundo.
#Proceso: Realiza la transformada de Fourier y calcula la frecuencia de esta.
#Salida: La transformada de Fourier de la señal y su frecuencia.
def Fourier(data,rate):
	transData = np.fft.fft(data)
	freq = np.fft.fftfreq(len(data),1/rate)
	return transData,freq

#Function:
#Process:
#Return:
def graphicFourier(data,rate,dataAM,rateAM,dataFM,rateFM,dataDemodulada,percentage):
	transData,freq = Fourier(data,rate)
	transDataAM,freqAM = Fourier(dataAM,rateAM)
	transDataFM,freqFM = Fourier(dataFM,rateFM)
	transDatademodulada,freqDemodulada = Fourier(dataDemodulada,rate)
	fig = plt.figure()
	fig.subplots_adjust(hspace=0.7, wspace=0.7)
	fig.add_subplot(411)
	plt.title("Señal Original")
	plt.xlabel("Frecuencia [Hz]")
	plt.ylabel("Amplitud [dB]")
	plt.plot(freq,abs(transData),'b')
	fig.add_subplot(412)
	plt.title("Transformada de Fourier con modulacion AM con "+ percentage)
	plt.xlabel("Frecuencia [Hz]")
	plt.ylabel("Amplitud [dB]")
	plt.plot(freqAM,abs(transDataAM),'g')
	fig.add_subplot(413)
	plt.title("Transformada de Fourier con modulacion FM al "+ percentage)
	plt.xlabel("Frecuencia [Hz]")
	plt.ylabel("Amplitud [dB]")
	plt.plot(freqFM,abs(transDataFM),'m')
	fig.add_subplot(414)
	plt.title("Transformada de Fourier señal demodulada al "+ percentage)
	plt.xlabel("Frecuencia [Hz]")
	plt.ylabel("Amplitud [dB]")
	plt.plot(freqDemodulada,abs(transDatademodulada),'r')
	plt.show()

rate,data = readFile("handel.wav")
data_interpol = interpolation(rate,data)

####################### MODULACION 100%#######################################
dataAM_1,portadoraAM_1,rateAM_1 = modulationAM(data_interpol,rate,1)
dataDemodulationAM_1 = demodulationAM(dataAM_1,rate,1)
filtered_1 = filtradoBajo(rate,dataDemodulationAM_1)
dataFM_1,portadoraFM_1,rateFM_1 = modulationFM(data_interpol,rate,1)
graphicAM(data,data_interpol,portadoraAM_1,dataAM_1,"100%")
graphicFM(data,data_interpol,portadoraFM_1,dataFM_1,"100%")
graphicFourier(data,rate,dataAM_1,rateAM_1,dataFM_1,rateFM_1,filtered_1,"100%")


####################### MODULACION 15%#######################################
dataAM_15,portadoraAM_15,rateAM_15 = modulationAM(data_interpol,rate,0.15)
dataDemodulationAM_15 = demodulationAM(dataAM_15,rate,0.15)
filtered_15 = filtradoBajo(rate,dataDemodulationAM_15)
dataFM_15,portadoraFM_15,rateFM_15 = modulationFM(data_interpol,rate,0.15)
graphicAM(data,data_interpol,portadoraAM_15,dataAM_15,"15%")
graphicFM(data,data_interpol,portadoraFM_15,dataFM_15,"15%")
graphicFourier(data,rate,dataAM_15,rateAM_15,dataFM_15,rateFM_15,filtered_15,"15%")


####################### MODULACION 125%#######################################
dataAM_125,portadoraAM_125,rateAM_125 = modulationAM(data_interpol,rate,1.25)
dataDemodulationAM_125 = demodulationAM(dataAM_125,rate,1.25)
filtered_125 = filtradoBajo(rate,dataDemodulationAM_125)
dataFM_125,portadoraFM_125,rateFM_125 = modulationFM(data_interpol,rate,1.25)
graphicAM(data,data_interpol,portadoraAM_125,dataAM_125,"125%")
graphicFM(data,data_interpol,portadoraFM_125,dataFM_125,"125%")
graphicFourier(data,rate,dataAM_125,rateAM_125,dataFM_125,rateFM_125,filtered_125,"125%")