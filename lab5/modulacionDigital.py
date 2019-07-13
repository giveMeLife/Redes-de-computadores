import numpy as np 
import matplotlib.pyplot as plt
import scipy.integrate as it
from scipy import interpolate, signal
import random


''' 
Función utilizada para simular un modulador ASK
Entrada: Un arreglo con bits, un arreglo con el tiempo que dura la transmisión y la frecuencia con la que se desea generar datos con la portadora
Proceso: Se crean dos portadoras con amplitudes distintas, y se analiza bit por bit, y según el bit se agrega en un arreglo de salida los valores aplicados 
         a dicha portadora
Salida: La salida de esta función es el arreglo con los datos generados por las portadoras y un arreglo de tiempo como eje X de dichos datos.
'''
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

''' 
Función utilizada para simular un demodulador ASK
Entrada: Un arreglo con los datos de las portadoras y la frecuencia que indica cada cuantos datos es un bit.
Proceso: Se analiza el arreglo por tramos, con la cantidad de elementos que corresponden a un bit, y según la amplitud máxima se define si corresponde
         a un 1 o a un 0
Salida: Se retorna un arreglo con los bits que se leen.
'''
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


'''
Función que agrega ruido gaussiano aditivo a una señal
Entrada: La señal a la que se le quiere agregar ruido, SNR y el tiempo en el que ocurre la señal
Proceso: Se genera ruido gaussiano aditivo con la función normal y luego se suma a la señal original
Salida: Señal con ruido
'''
def ruido(señal, snr, time):
    media = 0
    for elemento in señal:
        media = media + elemento
    media = media/señal.size
    energia = it.simps(señal,time)
    varianza = np.sqrt([energia/snr])

    ruido = np.random.normal(media, varianza, señal.size)
    return señal+ruido


'''
Función que genera un gráfico de bits o señal digital
Entradas: Arreglod e bits, tiempo en el que se envían, título del gráfico
Proceso: Se realiza el gráfico con stem
Salida:
'''
def plotDigital(bits, time, title):
    plt.xlabel('Tiempo')
    plt.ylabel('bit')
    plt.title(title)
    plt.stem(time, bits)
    plt.show()

'''
Función que genera un gráfico x vs y
Entradas: Arreglo con datos de la señal, tiempo en el que se envían, título del gráfico
Proceso: Se realiza el gráfico simple con plot
Salida:
'''
def plotNormal(signal, time, title):
    plt.xlabel('Tiempo')
    plt.ylabel('Energía')
    plt.title(title)
    plt.plot(time,signal)
    plt.show()

'''
Función que genera un gráfico de barra con la relación del error (BER) y SNR
Entrada: Valores de error y valores de SNR
Proceso: Realiza gráficos de barra comparativos
Salida:
'''
def graficoError(valuesE, valuesS):
    barWidth = 0.25
    r1 = np.arange(valuesE.size)
    r2 = [x + barWidth for x in r1]
    plt.bar(r1, valuesE, color='#6A5ACD', width=barWidth, label="Error")
    plt.bar(r2, valuesS, color='#6495ED', width=barWidth, label="SNR")
    plt.xlabel("Pruebas")
    plt.xticks([r + barWidth for r in range(valuesE.size)], ['Arreglo de bits 1', 'Arreglo de bits 2', 'Arreglo de bits 3'])
    plt.ylabel("Grado")
    plt.title("Representación relación entre SNR y Error de recepciónd e bits")
    plt.legend()
    plt.show()


'''
Función que genera un arreglo con bits aleatorio 
Entrada: Largo (cantidad de bits que se desean)
Proceso: Se genera un arreglo de largo ingresado con valores 0 o 1
Salida: Arreglo con bits

'''
def generarAleatorio(largo):
    l = np.random.randint(2,size=largo)
    return l


''' 
Función que dadodos arreglos, calcula sus diferencias, en este caso para dos arreglos de bits calcula el BER
Entrada: Dos arreglos con bits
Proceso: Cuenta los valores distintos y lo divide por la cantidad de valores
Salida: Error
'''
def calculoError(original, ruidosa):
    diferencias = np.sum(original != ruidosa)
    error = diferencias/original.size*1.0
    return error


########################################    MAIN    ########################################


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
errores = []
snr = []

time1 = np.linspace(0,bits1.size,bits1.size)
plotDigital(bits1,time1, "Bits enviados 10^3")
salida1, t1 = ask(bits1,1,20)
señalRuidosa1 = ruido(salida1, 1, t1)
rbits1 = askReceptor(señalRuidosa1,20)
error1 = calculoError(bits1,rbits1)
print(error1)
snr.append(1/7.0)
errores.append(error1)

time2 = np.linspace(0,bits2.size,bits2.size)
plotDigital(bits2,time2, "Bits enviados 10^3")
salida2, t2 = ask(bits2,1,20)
señalRuidosa2 = ruido(salida2, 4, t2)
rbits2 = askReceptor(señalRuidosa2,20)
error2 = calculoError(bits2,rbits2)
print(error2)
snr.append(4/7.0)
errores.append(error2)

time3 = np.linspace(0,bits3.size,bits3.size)
plotDigital(bits3,time3, "Bits enviados 10^3")
salida3, t3 = ask(bits3,1,20)
señalRuidosa3 = ruido(salida3, 7, t3)
rbits3 = askReceptor(señalRuidosa3,20)
error3 = calculoError(bits3,rbits3)
print(error3)
snr.append(7/7.0)
errores.append(error3)
errores = np.array(errores)
snr = np.array(snr)
graficoError(errores, snr)