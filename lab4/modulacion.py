import numpy as np 
import matplotlib.pyplot as py
import scipy.io.wavfile as wavfile

def readFile(nombre):
	sound = wavfile.read(nombre)
	return sound

data = readFile("handel.wav")

