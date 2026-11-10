# CARGA DO CAPACITOR - CORRENTE certo

import matplotlib.pyplot as plt
import numpy as np 

tensao = 12
resistencia = 47000
capacitancia = 0.0022
neper = 2.71828
tal = resistencia*capacitancia

tempo = np.linspace(0, 5*tal, 30)
plt.plot(tempo,(tensao/resistencia) * (neper ** (-tempo/tal)))

plt.title("Carga do Capacitor - Corrente")
plt.xlabel("Tal (s)")
plt.ylabel("Corrente")
plt.show()