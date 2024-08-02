#Exercício 19: Você tem uma lista de 1000 números inteiros aleatórios entre 1 e
#1000.
#Pegue uma amostra de 50 números dessa lista. Calcule a média e o desvio
#padrão da amostra.
#Escreva o programa em Python.

import random

# Gerar uma lista com 50 números inteiros únicos aleatórios entre 1 e 1000
lista_numeros = random.sample(range(1, 1001), 50)

print(f"Aqui estão os números selecionados da lista: {lista_numeros}")

#Cálculo da média
soma = sum(lista_numeros)
media = soma /len(lista_numeros)

print(f"A média destes números é de: {media}")
#-------------------------------------------------------

#Calculando a variância amostral para depois calcular o desvio padrão

soma_numeros = sum((x - media)** 2 for x in lista_numeros)

variancia_amostral = soma_numeros / (len(lista_numeros) -1)

#Desvio padrão: 

import math

desvio_padrao = math.sqrt(variancia_amostral)

print(f"O desvio padrão da amostra é: {desvio_padrao:.2f}")

