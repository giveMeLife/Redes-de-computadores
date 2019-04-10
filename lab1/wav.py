import numpy
import matplotlib
import scipy.io.wavfile as wavfile

sound = wavfile.read("handel.wav");
print(sound[1])