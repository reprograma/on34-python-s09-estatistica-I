#Exercício 14: Suponha que em uma urna há 3 bolas vermelhas e 2 bolas azuis.
#Qual é a probabilidade de retirar uma bola vermelha ou uma bola azul?
#Resolva e escreva o programa em Python.

prob_vermelha = 3/5
prob_azul = 2/5

prob_total = (prob_vermelha + prob_azul) * 100
print (f"A probabilidade de retirar uma bola vermelha ou azul é: {prob_total:.1f}%")
