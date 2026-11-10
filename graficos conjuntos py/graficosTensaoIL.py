import matplotlib.pyplot as plt
import numpy as np 
plt.figure(figsize = ((12, 6)))

tensao = 12
resistencia = 470
indutancia = 0.01
neper = 2.71828
tal = indutancia/resistencia

# CARGA DO INDUTOR - TENSAO

tempo = np.linspace(0, 5*tal, 30)
plt.subplot(1, 2, 1)
plt.plot(tempo,tensao * (neper ** (-tempo/tal)))

plt.title("Carga do Indutor - Tensao")
plt.xlabel("Tal (s)")
plt.ylabel("Tensao")

# DESCARGA DO INDUTOR - TENSAO

tempo = np.linspace(0, 5*tal, 30)
plt.subplot(1, 2, 2)
plt.plot(tempo,(-tensao) * (neper ** (-tempo/tal)))

plt.title("Descarga do Indutor - Tensao")
plt.xlabel("Tal (s)")
plt.ylabel("Tensao")

plt.show()