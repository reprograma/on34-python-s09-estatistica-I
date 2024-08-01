#Exercício 13: Dada a amostra \([50, 52, 55, 57, 60, 62, 65, 68, 70, 72]\), calcule
#a variância amostral e o desvio padrão amostral.

amostra = [50,52,55,57,60,62,65,68,70,72]
media = sum(amostra) / len(amostra)

soma_quadrados = sum((x - media)** 2 for x in amostra)

variancia_amostral = soma_quadrados/ (len(amostra) -1)

print(f"A variância amostral desta amostra é: {variancia_amostral:.3}")

#Desvio padrão: 

import math

desvio_padrao = math.sqrt(variancia_amostral)

print(f"O desvio padrão da amostra é: {desvio_padrao:.3}")