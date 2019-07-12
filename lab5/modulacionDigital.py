import numpy as np 
import matplotlib.pyplot as plt
import scipy.integrate as it
from scipy import interpolate, signal
import random

def ask(bits, tiempo, frec):
    time = np.linspace(0,tiempo,frec)
    port1 = 1*np.cos(2*np.pi*time*frec*2)
    port2 = 0.5*np.cos(2*np.pi*time*frec*2)
    l = []
    salida = np.array(l)
    i = 0
    for bit in bits:
        if bit == 0:
            for a in port2:
                salida = np.append(salida,a)
        else:
            for a in port1:
                salida = np.append(salida,a)
    
    t = np.linspace(0,tiempo*len(bits),salida.size)
    return salida,t

def askReceptor(señal, frec):
    l = []
    Iindex = 0
    Findex = 20
    tramos = señal.size/frec
    for i in range(0,int(tramos)):
        data = señal[Iindex:Findex]
        if(np.amax(data)-1<=0.3 and np.amax(data)-1>=0 ):
            l.append(1)
        else:
            l.append(0)
        Iindex = Iindex + 20
        Findex = Findex + 20
    salida = np.array(l)
    return salida


def ruido(señal, snr, time):
    media = 0
    for elemento in señal:
        media = media + elemento
    media = media/señal.size
    energia = it.simps(señal,time)
    varianza = np.sqrt([energia/snr])

    ruido = np.random.normal(media, varianza, señal.size)
    return señal+ruido



def plotDigital(bits, time, title):
    plt.xlabel('Tiempo')
    plt.ylabel('bit')
    plt.title(title)
    plt.stem(time, bits)
    plt.show()

def plotNormal(signal, time, title):
    plt.xlabel('Tiempo')
    plt.ylabel('Energía')
    plt.title(title)
    plt.plot(time,signal)
    plt.show()

def generarAleatorio(largo):
    l = np.random.randint(2,size=largo)
    return l

def calculoError(original, ruidosa):
    diferencias = np.sum(original == ruidosa)
    error = diferencias/original.size  
    return error


''' Aplicación para caso simple'''
#Se aplica ASK y se muestra el resultado
#Bits usados para prueba inicial
bits = np.array([0,1,1,0,1,0])
time = np.linspace(0,6,6)
#Se grafica los bits enviados
plotDigital(bits,time, "Bits enviados inicialmente")

salida, t = ask(bits,1,20)
plotNormal(salida, t, "Señal demodulada sin ruido")

#Se recibe los valores de ask y se muestra el resultado
rbits = askReceptor(salida,20)
plotDigital(bits,time, "Digitalización sin ruido")

#Se aplica ruido a la señal
señalRuidosa = ruido(salida,2,t)
plotNormal(señalRuidosa, t, "Señal demodulada con ruido")

#Se grafica la salida con ruido
rbits1 = askReceptor(señalRuidosa,20)
plotDigital(bits,time, "Digitalización con ruido")

#############################FIN EJEMPLOM SIMPLE###############################

bits1 = generarAleatorio(10**3)
bits2 = generarAleatorio(10**3)
bits3 = generarAleatorio(10**3)


time1 = np.linspace(0,bits1.size,bits1.size)
plotDigital(bits1,time1, "Bits enviados 10^3")
salida1, t1 = ask(bits1,1,20)
señalRuidosa1 = ruido(salida1, 4, t1)
rbits1 = askReceptor(señalRuidosa,20)
error1 = calculoError(bits1,rbits1)
print(error1)


time2 = np.linspace(0,bits2.size,bits2.size)
plotDigital(bits2,time2, "Bits enviados 10^3")
salida2, t2 = ask(bits2,1,20)
señalRuidosa2 = ruido(salida2, 2, t2)
rbits2 = askReceptor(señalRuidosa2,20)
error2 = calculoError(bits2,rbits2)
print(error2)

time3 = np.linspace(0,bits3.size,bits3.size)
plotDigital(bits3,time3, "Bits enviados 10^3")
salida3, t3 = ask(bits3,1,20)
señalRuidosa3 = ruido(salida3, 1, t3)
rbits3 = askReceptor(señalRuidosa3,20)
error3 = calculoError(bits3,rbits3)
print(error3)