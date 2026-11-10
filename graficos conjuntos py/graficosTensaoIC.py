import matplotlib.pyplot as plt
import numpy as np 
plt.figure(figsize = ((12, 6)))

tensao = 12
resistencia = 47000
capacitancia = 0.0022
neper = 2.71828
tal = resistencia*capacitancia

# CARGA DO CAPACITOR - TENSAO

tempo = np.linspace(0, 5*tal, 30)
plt.subplot(1, 2, 1)
plt.plot(tempo,tensao*(1-neper**(-tempo/(tal))))

plt.title("Carga do Capacitor - Tensao")
plt.xlabel("Tal (s)")
plt.ylabel("Tensao")

# DESCARGA DO CAPACITOR - TENSAO

tempo = np.linspace(0, 5*tal, 30)
plt.subplot(1, 2, 2)
plt.plot(tempo,tensao*(neper**(-tempo/(tal))))

plt.title("Descarga do Capacitor - Tensao")
plt.xlabel("Tal (s)")
plt.ylabel("Tensao")

plt.show()