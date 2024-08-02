#Exercício 8: Análise de Temperaturas
#Você foi contratado para analisar dados meteorológicos.
#Você tem uma lista com as temperaturas registradas em uma cidade durante
#um mês. Escreva um programa em Python que:

#1. Calcule a média aritmética das temperaturas.

temp1 = 32
temp2 = 25
temp3 = 10
temp4 = 23

media = int(temp1+temp2+temp3+temp4)/4
print(f"A média aritmética das temperaturas é de: {media}")

#2. Encontre a mediana das temperaturas.

temperaturas = [temp1, temp2, temp3, temp4]
temperaturas.sort() #Organizo em ordem crescente as temperaturas
tamanho = len(temperaturas) #Descubro o número de elementos que tem dentro da minha lista
mediana = (temperaturas [tamanho //2-1] + temperaturas[tamanho //2]) /2
print(f"A mediana das temperaturas é: {mediana}")

#3. Determine a moda das temperaturas (se houver).

temperaturas = [temp1, temp2, temp3, temp4]
frequencia ={}
for num in temperaturas:
    if num in frequencia:
        frequencia[num]+=1
    else:
        frequencia[num]=1
    
max_frequencia = max(frequencia.values())

if max_frequencia == 1:
    moda = "Não há moda"
else: moda = [num for num, freq in frequencia.items() if freq == max_frequencia]

print(f"A moda é: {moda}")