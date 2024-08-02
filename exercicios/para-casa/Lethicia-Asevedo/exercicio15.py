#Exercício 15: Um dado justo de 6 faces é lançado. Qual é a probabilidade de
#obter um número par ou um número menor que 4?
#Resolva e escreva o programa em Python.

prob_par = 3/6
prob_menor_4 = 3/6

prob_total = (prob_par + prob_menor_4) * 100

print(f"A probabilidade de obter um número par ou um número menor que 4 é de: {prob_total:.2f} %")