# DESCARGA DO CAPACITOR - TENSAO certo

import matplotlib.pyplot as plt
import numpy as np 

tensao = 12
resistencia = 47000
capacitancia = 0.0022
neper = 2.71828
tal = resistencia*capacitancia

tempo = np.linspace(0, 5*tal, 30)
plt.plot(tempo,tensao*(neper**(-tempo/(tal))))

plt.title("Descarga do Capacitor - Tensao")
plt.xlabel("Tal (s)")
plt.ylabel("Tensao")
plt.show()