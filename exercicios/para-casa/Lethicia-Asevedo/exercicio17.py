#Exercício 17: Você lança uma moeda justa e, em seguida, lança um dado justo.
#Qual é a probabilidade de obter cara na moeda e um número maior que 4 no
#dado?
#Resolva e escreva o programa em Python.

prob_cara = 1/2
prob_dado = 2/6

prob_total = (prob_cara * prob_dado) *100

print(f"A probabilidade obter cara na moeda e um número maior que 4 no dado é de: {prob_total:.2f}")


