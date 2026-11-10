# DESCARGA DO INDUTOR - TENSAO

import matplotlib.pyplot as plt
import numpy as np 

tensao = 12
resistencia = 470
indutancia = 0.01
neper = 2.71828
tal = indutancia/resistencia

tempo = np.linspace(0, 5*tal, 30)
plt.plot(tempo,(-tensao) * (neper ** (-tempo/tal)))

plt.title("Descarga do Indutor - Tensao")
plt.xlabel("Tal (s)")
plt.ylabel("Tensao")
plt.show()