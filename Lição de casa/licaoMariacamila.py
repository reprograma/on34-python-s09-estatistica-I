
#Exercício 1
#A - Quantitativo, discreto;
#B - Qualitativa, ordinal;
#C - Quantitativo, contínua;
#D - Qualitativa, nominal;
#E - Quantitativa, contínua.

#Exercício 2
#A - Qualitativo, nominal;
#B - Quantitativo, discreto;
#C - Quantitativo, discreto;
#D - Quantitativo, contínua;
#E - Qualitativo, ordinal;
#F - Quantitativo, discreto.


#Exercício 3
numeros = [10, 20, 30, 40,50]
soma = sum(numeros)
quantidade = len(numeros)
media = soma / quantidade
#print("A média dos números é", media)

#Exercício 4 
numeros = [1, 3, 4, 2, 5]
numeros.sort()
#print(numeros)
tamanho = len(numeros)
#print(tamanho)
mediana = numeros[tamanho // 2]
#print("Mediana:", mediana)

#Exercício 5
numeros = [1, 2, 2, 3, 4, 4, 4, 5, 5]
frequencia = {}
for num in numeros:
    if num in frequencia:
        frequencia[num] += 1
    else:
        frequencia[num] = 1
max_frequencia = max(frequencia.values())
moda = [num for num, freq in frequencia.items() if freq == max_frequencia]
#print("Moda:", moda)

#Exercício 6
notas = [10, 9, 3, 3, 3, 4, 5, 7]
soma = 0
for nota in notas:
    soma += nota
    media = soma / len(notas)
    #print("A média aritmética das notas é", media)

notas.sort()
tamanho = len(notas)
mediana = (notas[tamanho // 2 -1] + notas[tamanho // 2]) / 2

frequencia = {}
for nta in notas:
    if nta in frequencia:
        frequencia[nta] += 1
    else:
        frequencia[nta] = 1
max_frequencia = max(frequencia.values())
moda = [nta for nta, freq in frequencia.items() if freq == max_frequencia]

#print(f"A mediana das notas é", mediana)
#print(f"A moda das notas é", moda)




#Exercício 7
produtos_vendas = [
    {'codigo': 'P001', 'vendas': 20},
    {'codigo': 'P002', 'vendas': 35},
    {'codigo': 'P003', 'vendas': 15},
    {'codigo': 'P004', 'vendas': 50},
    {'codigo': 'P005', 'vendas': 50},
    {'codigo': 'P006', 'vendas': 20},
    {'codigo': 'P007', 'vendas': 50}
]
unidades_vendidas = [produto['vendas'] for produto in produtos_vendas]
soma = sum(unidades_vendidas)
quantidade = len(unidades_vendidas)
media = soma / quantidade

unidades_vendidas.sort()
if quantidade % 2 == 0:
    mediana = (unidades_vendidas[quantidade // 2 - 1] + unidades_vendidas[quantidade // 2]) / 2
else:
    mediana = unidades_vendidas[quantidade // 2]

frequencia = {}
for vendas in unidades_vendidas:
    if vendas in frequencia:
        frequencia[vendas] += 1
    else:
        frequencia[vendas] = 1
moda = None
max_frequencia = 0
for vendas, freq in frequencia.items():
    if freq > max_frequencia:
        moda = vendas
        max_frequencia = freq


#print(f"A média aritmética das unidades vendidas é", media)
#print(f"A mediana das unidades vendidas é", mediana)
#print(f"O produtos mais vendido foi o", moda)

#Exercício 8
temperaturas = [26.5, 27.0, 7.0, 21.0]
soma = 0
for temperatura in temperaturas:
    soma += temperatura
    media = soma / len(temperaturas)
    #print("A média aritmética da temperatura é", media)


temperaturas.sort()
tamanho = len(temperaturas)
mediana = (temperaturas[tamanho // 2 - 1] + temperaturas[tamanho // 2]) / 2


frequencia = {}
for temp in temperaturas:
    if temp in frequencia:
        frequencia[temp] += 1
    else:
        frequencia[temp] = 1
max_frequencia = max(frequencia.values())
if max_frequencia == 1:
    moda = "Nenhuma moda encontrada"
else:
    moda = [temp for temp, freq in frequencia.items() if freq == max_frequencia]
               

#print(f"A mediana das temperaturas é", mediana)
#print(f"Moda:", moda)  

#Exercício 9
amostra = ([12, 15, 20, 22, 30])
media = sum(amostra) / len(amostra)
soma_quadrados = sum((x -media)** 2 for x in amostra)
variancia_amostral = soma_quadrados / (len(amostra) - 1)
#print("A Variância Amostral é", variancia_amostral)

import math
n = len(amostra)
media = sum(amostra) / n
soma_dos_quadrados = sum((x - media) ** 2 for x in amostra)
variancia_amostral = soma_dos_quadrados / (n - 1)
desvio_padrao_amostral = math.sqrt(variancia_amostral)
#print(f"O Desvio Padrão amostral é {desvio_padrao_amostral:.2f}")

#Exercício 10
amostra2 = ([5, 7, 9, 10, 15, 18])
media = sum(amostra2) / len(amostra2)
soma_quadrados = sum((x -media)** 2 for x in amostra2)
variancia_amostral = soma_quadrados / (len(amostra) - 1)
#print("A Variância Amostral é", variancia_amostral)

import math
n = len(amostra2)
media = sum(amostra2) / n
soma_dos_quadrados = sum((x - media) ** 2 for x in amostra2)
variancia_amostral = soma_dos_quadrados / (n - 1)
desvio_padrao_amostral = math.sqrt(variancia_amostral)
#print(f"O Desvio Padrão amostral é {desvio_padrao_amostral}")

#Exercício 11
amostra3 = ([23, 29, 31, 35, 40, 42, 50])
media = sum(amostra3) / len(amostra3)
soma_quadrados = sum((x -media)** 2 for x in amostra3)
variancia_amostral = soma_quadrados / (len(amostra3) - 1)
#print("A Variância Amostral é", variancia_amostral)

import math
n = len(amostra3)
media = sum(amostra3) / n
soma_dos_quadrados = sum((x - media) ** 2 for x in amostra3)
variancia_amostral = soma_dos_quadrados / (n - 1)
desvio_padrao_amostral = math.sqrt(variancia_amostral)
#print(f"O Desvio Padrão amostral é {desvio_padrao_amostral:.2f}")

#Exercício 12
amostra4 = ([3, 6, 8, 10, 12, 14, 16, 18])
media = sum(amostra4) / len(amostra4)
soma_quadrados = sum((x -media)** 2 for x in amostra4)
variancia_amostral = soma_quadrados / (len(amostra4) - 1)
#print("A Variância Amostral é", variancia_amostral)

import math
n = len(amostra4)
media = sum(amostra4) / n
soma_dos_quadrados = sum((x - media) ** 2 for x in amostra4)
variancia_amostral = soma_dos_quadrados / (n - 1)
desvio_padrao_amostral = math.sqrt(variancia_amostral)
#print(f"O Desvio Padrão amostral é {desvio_padrao_amostral:.2f}")

#Exercício 13
amostra5 = ([50, 52, 55, 57, 60, 62, 65, 68, 70, 72])
media = sum(amostra5) / len(amostra5)
soma_quadrados = sum((x -media)** 2 for x in amostra5)
variancia_amostral = soma_quadrados / (len(amostra5) - 1)
#print("A Variância Amostral é", variancia_amostral)

import math
n = len(amostra5)
media = sum(amostra5) / n
soma_dos_quadrados = sum((x - media) ** 2 for x in amostra5)
variancia_amostral = soma_dos_quadrados / (n - 1)
desvio_padrao_amostral = math.sqrt(variancia_amostral)
#print(f"O Desvio Padrão amostral é {desvio_padrao_amostral}")

#Exercício 14
prob_bola = 5 / 5
#print(f"Probabilidade de sair bola azul ou vermelha: {prob_bola * 100}%")

#Exercício 15
prob_par = 3 / 6
prob_menor_que_4 = 3 / 6 
prob_par_e_menor_que_4 = 1 / 6
prob_par_ou_menor_que_4 = prob_par + prob_menor_que_4 - prob_par_e_menor_que_4
#print(f"Probabilidade de obter um número par ou menor que 4: {prob_par_ou_menor_que_4 * 100:.2f}%")

#Exercício 16
prob_menor_que_4 = 3 / 10
prob_maior_que_7 = 3 / 10
prob_menor_que_4_e_maior_que_7 = 0
prob_menor_que_4_ou_maior_que_7 = prob_menor_que_4 + prob_maior_que_7 - prob_menor_que_4_e_maior_que_7
#print(f"Probabilidade de obter um número menor que 4 ou maior que 7: {prob_menor_que_4_ou_maior_que_7 * 100:.2f}%")

#Exercício 17
prob_cara = 1 / 2
prob_maior_que_4 = 2 / 6
prob_cara_e_maior_que_4 = prob_cara * prob_maior_que_4
#print(f"Probabilidade de obter cara na moeda e um número maior que 4 no dado: {prob_cara_e_maior_que_4 * 100:.2f}%")

#Exercício 18
prob_camiseta_azul = 4 / 10
prob_sapatos_pretos = 3 / 8
prob_camiseta_azul_e_sapatos_pretos = prob_camiseta_azul * prob_sapatos_pretos
#print(f"Probabilidade de escolher uma camiseta de cor azul e um par de sapatos pretos: {prob_camiseta_azul_e_sapatos_pretos * 100:.2f}%")

#Exercicio 19

import random
import math

lista_numeros = [random.randint(1, 1000) for _ in range(1000)]
amostra = random.sample(lista_numeros, 50)
media_amostra = sum(amostra) / len(amostra)
#print(f"Média da amostra: {media_amostra:.2f}")
soma_quadrados = sum((x - media_amostra) ** 2 for x in amostra)
variancia_amostral = soma_quadrados / (len(amostra) - 1)
#print(f"Variância amostral: {variancia_amostral:.2f}")
desvio_padrao_amostral = math.sqrt(variancia_amostral)
#print(f"Desvio padrão amostral: {desvio_padrao_amostral:.2f}")

#Exercicio 20
import random

populacao = [('A', 100), ('B', 200), ('C',300)]

porcentagem = 10

amostra_total = []
for grupo, tamanho in populacao:
    tamanho_amostra = int(tamanho * porcentagem / 100)
    itens = [f"{grupo}_item_{i}" for i in range(tamanho)]
    amostra_estratificada = random.sample(itens, tamanho_amostra)
    amostra_total.extend(amostra_estratificada)
    
#print(f"Amostra total (10% de cada grupo): {amostra_total}")



