import matplotlib.pyplot as plt
import numpy as np 
plt.figure(figsize = ((12, 6)))

tensao = 12
resistencia = 470
indutancia = 0.01
neper = 2.71828
tal = indutancia/resistencia

# CARGA DO INDUTOR - CORRENTE

tempo = np.linspace(0, 5*tal, 30)
plt.subplot(1, 2, 1)
plt.plot(tempo,(tensao/resistencia) * (1 - (neper ** (-tempo/tal))))

plt.title("Carga do Indutor - Corrente")
plt.xlabel("Tal (s)")
plt.ylabel("Corrente")

# DESCARGA DO INDUTOR - CORRENTE

tempo = np.linspace(0, 5*tal, 30)
plt.subplot(1, 2, 2)
plt.plot(tempo,(tensao/resistencia) * (neper ** (-tempo/tal)))

plt.title("Descarga do Indutor - Corrente")
plt.xlabel("Tal (s)")
plt.ylabel("Corrente")

plt.show()