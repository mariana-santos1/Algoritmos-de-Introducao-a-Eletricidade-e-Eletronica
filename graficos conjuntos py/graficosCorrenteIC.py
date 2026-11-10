import matplotlib.pyplot as plt
import numpy as np 
plt.figure(figsize = ((12, 6)))

tensao = 12
resistencia = 47000
capacitancia = 0.0022
neper = 2.71828
tal = resistencia*capacitancia

# CARGA DO CAPACITOR - CORRENTE

tempo = np.linspace(0, 5*tal, 30)
plt.subplot(1, 2, 1)
plt.plot(tempo,(tensao/resistencia) * (neper ** (-tempo/tal)))

plt.title("Carga do Capacitor - Corrente")
plt.xlabel("Tal (s)")
plt.ylabel("Corrente")

# DESCARGA DO CAPACITOR - CORRENTE

tempo = np.linspace(0, 5*tal, 30)
plt.subplot(1, 2, 2)
plt.plot(tempo,-(tensao/resistencia) * (neper ** (-tempo/tal)))


plt.title("Descarga do Capacitor - Corrente")
plt.xlabel("Tal (s)")
plt.ylabel("Corrente")

plt.show()