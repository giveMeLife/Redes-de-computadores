import numpy as np 
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from scipy import interpolate, signal


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
    print(tramos)
    for i in range(0,int(tramos)):
        data = señal[Iindex:Findex]
        if(np.amax(data)==1.0):
            l.append(1)
        else:
            l.append(0)
        Iindex = Iindex + 20
        Findex = Findex + 20
    salida = np.array(l)
    return salida

def plotDigital(bits, time):
    plt.xlabel('Tiempo')
    plt.ylabel('bit')
    plt.title(r'Señal digital')
    plt.stem(time, bits)
    plt.show()

def plotNormal(signal, time):
    plt.xlabel('Tiempo')
    plt.ylabel('Energía')
    plt.plot(time,signal)
    plt.show()

#Bits usados para prueba inicial
bits = np.array([0,1,1,0,1,0])
time = np.linspace(0,6,6)
#Se grafica los bits enviados
plotDigital(bits,time)


#Se aplica ASK y se muestra el resultado
salida, t = ask(bits,1,20)
plotNormal(salida, t)

#Se recibe los valores de ask y se muestra el resultado
rbits = askReceptor(salida,20)
plotDigital(bits,time)