# Capacitor: dados
tensao = 12
resistencia = 47000
capacitancia = 0.0022
neper = 2.71828
tal = resistencia*capacitancia
tempo1 = tal/30
tempo = tempo1
cont = 1

while cont <= 30:
    vCarregamento = tensao * (1 - (neper ** (-tempo/tal)))
    print(cont, ':', vCarregamento, 'em', tempo, 'segundos')
    tempo = tempo + tempo1
    cont = cont + 1