#Exercício 11: Considere a amostra \([23, 29, 31, 35, 40, 42, 50]\). Determine a
#variância amostral e o desvio padrão amostral.

#Variância amostral: 

amostra = [23,29,31,35,40,42,50]
media = sum(amostra) / len(amostra)

soma_quadrados = sum((x - media)** 2 for x in amostra)

variancia_amostral = soma_quadrados/ (len(amostra) -1)

print(f"A variância amostral desta amostra é: {variancia_amostral:.3}")

#Desvio padrão: 

import math

desvio_padrao = math.sqrt(variancia_amostral)

print(f"O desvio padrão da amostra é: {desvio_padrao:.3}")