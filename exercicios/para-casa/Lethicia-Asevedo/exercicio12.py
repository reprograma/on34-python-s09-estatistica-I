#Exercício 12: Para a amostra \([3, 6, 8, 10, 12, 14, 16, 18]\), calcule a variância
#amostral e o desvio padrão amostral.

amostra = [3,6,8,10,12,14,16,18]
media = sum(amostra) / len(amostra)

soma_quadrados = sum((x - media)** 2 for x in amostra)

variancia_amostral = soma_quadrados/ (len(amostra) -1)

print(f"A variância amostral desta amostra é: {variancia_amostral:.3}")

#Desvio padrão: 

import math

desvio_padrao = math.sqrt(variancia_amostral)

print(f"O desvio padrão da amostra é: {desvio_padrao:.3}")