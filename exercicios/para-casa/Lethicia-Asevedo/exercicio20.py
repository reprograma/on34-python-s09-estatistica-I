#Exercício 20: Considere uma população com 3 grupos (A, B, C) com tamanhos
#diferentes: A (100), B (200), C (300).
#Faça uma amostra estratificada onde você tira 10% de cada grupo.
#Escreva o programa em Python.


import random

populacao = [('A', 100), ('B', 200), ('C', 300)]

# Função para gerar amostras estratificadas
def amostra_estratificada(populacao, percentual):
    amostras = []
    for grupo, tamanho in populacao:
        # Gerar lista de elementos para o grupo
        grupo_lista = list(range(1, tamanho + 1))
        # Calcular o tamanho da amostra para o grupo
        tamanho_amostra = int(percentual * tamanho)
        # Selecionar a amostra
        amostra = random.sample(grupo_lista, tamanho_amostra)
        # Adicionar a amostra à lista de amostras
        amostras.append((grupo, amostra))
    return amostras

# Definir o percentual da amostra (10%)
percentual_amostra = 0.10

# Obter a amostra estratificada
amostras_estratificadas = amostra_estratificada(populacao, percentual_amostra)

for grupo, amostra in amostras_estratificadas:
    print(f"Amostra do Grupo {grupo} ({int(percentual_amostra * 100)}%): {amostra}")


