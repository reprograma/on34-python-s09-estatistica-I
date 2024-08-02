#Exercício 6: Análise de Notas de Alunos
#Uma escola precisa analisar o desempenho dos alunos em uma prova. As
#notas dos alunos são armazenadas em uma lista. Escreva um programa em
#Python que:
#1. Calcule a média aritmética das notas.
#2. Encontre a mediana das notas.
#3. Determine a moda das notas (a nota que aparece com maior frequência).


##Calculando a média das notas inseridas:
nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
nota3 = int(input("Insira a terceira nota: "))
nota4 = int(input("Insira a quarta nota: "))
nota5 = int(input("Insira a quinta nota: "))
nota6 = int(input("Insira a sexta nota: "))
nota7 = int(input("Insira a sétima nota: "))
nota8 = int(input("Insira a oitava nota: "))
nota9 = int(input("Insira a nona nota: "))
media = (nota1+nota2+nota3+nota4+nota5+nota6+nota7+nota9) / 9

print (f"A média das notas inseridas é: {media:.2f}")

##Calculando a mediana das notas inseridas:
mediana = [nota1,nota2,nota3,nota4,nota5,nota6,nota7,nota9]
mediana.sort()
tamanho = len(mediana)
mediana = mediana[tamanho //2]

print(f"A mediana das notas inseridas é: {mediana}")

#Calculando a moda dos números inseridos:

numeros = [nota1,nota2,nota3,nota4,nota5,nota6,nota7,nota9]
frequencia = {}
for num in numeros:
    if num in frequencia:
        frequencia[num]+=1
    else:
        frequencia[num]=1

max_frequencia = max(frequencia.values())

modas = [num for num, freq in frequencia.items() if freq == max_frequencia]

print(f"A(s) moda(s) das notas inseridas é(são): {modas}")