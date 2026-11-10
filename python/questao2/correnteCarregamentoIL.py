# Indutor: dados
tensao = 12
resistencia = 470
indutancia = 0.01
neper = 2.71828
tal = indutancia/resistencia
tempo1 = tal/30
tempo = tempo1
cont = 1

while cont <= 30:
    iCarregamento = (tensao/resistencia) * (1 - (neper ** (-tempo/tal)))
    print(cont, ':', iCarregamento, 'em', tempo, 'segundos')
    tempo = tempo + tempo1
    cont = cont + 1