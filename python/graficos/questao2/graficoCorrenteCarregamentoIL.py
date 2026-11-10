# CARGA DO INDUTOR - CORRENTE certo

import matplotlib.pyplot as plt
import numpy as np 

tensao = 12
resistencia = 470
indutancia = 0.01
neper = 2.71828
tal = indutancia/resistencia

tempo = np.linspace(0, 5*tal, 30)
plt.plot(tempo,(tensao/resistencia) * (1 - (neper ** (-tempo/tal))))

plt.title("Carga do Indutor - Corrente")
plt.xlabel("Tal (s)")
plt.ylabel("Corrente")
plt.show()
