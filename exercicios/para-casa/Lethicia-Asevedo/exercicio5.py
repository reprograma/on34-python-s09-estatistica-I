#Exercício 5: Cálculo da Moda
#Dado um conjunto de números, encontre a moda. A moda é o número que
#aparece com maior frequência no conjunto.
#Conjunto: `[1, 2, 2, 3, 4, 4, 4, 5, 5]`

numeros = [1, 2, 2, 3, 4, 4, 4, 5, 5]

frequencia = {}
for num in numeros:
    if num in frequencia:
        frequencia[num]+=1
    else:
        frequencia[num]=1

print(frequencia)


#Encontrar a maior frquência
max_frequencia = max(frequencia.values())
print(max_frequencia)


#Encontrar todas as modas
modas = [num for num, freq in frequencia.items() if freq == max_frequencia]

print(f"A moda dessa lista é: {modas}")