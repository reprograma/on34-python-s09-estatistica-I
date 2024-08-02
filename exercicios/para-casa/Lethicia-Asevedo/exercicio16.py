#Exercício 16: Uma caixa contém 10 bilhetes numerados de 1 a 10.
#Qual é a probabilidade de retirar um bilhete que tenha um número menor que 4
#ou um número maior que 7?
#Resolva e escreva o programa em Python.

prob_menor_4 = 3/10
prob_maior_7 = 3/10

prob_total = (prob_menor_4 + prob_maior_7) * 100

print(f"A probabilidade de tirar um número menor que 4 ou maior que 7 é de: {prob_total:.2f}%")