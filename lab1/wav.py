import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile

sound = wavfile.read("handel.wav")
print(sound[1].size)
x = np.linspace(0,sound[1].size/sound[0],sound[1].size)
y=sound[1]
plt.plot(x,y)
plt.xlabel("Tiempo (s)")
plt.ylabel("Muestra")
plt.show()
