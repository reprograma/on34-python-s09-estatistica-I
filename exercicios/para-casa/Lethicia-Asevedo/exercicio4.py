#Exercício 4: Cálculo da Mediana
#Dado um conjunto de números, calcule a mediana. A mediana é o valor central
#de um conjunto de números ordenados.
#Conjunto: `[1, 3, 4, 2, 5]`

mediana = [1,2,3,4,5]
mediana.sort()
tamanho = len(mediana)
mediana = mediana[tamanho//2]

print(f"A mediana do conjunto de números dado é: {mediana}" )


