#Exercício 9: Você tem a seguinte amostra de dados: \([12, 15, 20, 22, 30]\).
#Calcule a variância amostral e o desvio padrão amostral usando Python.

#Variância amostral: 

amostra = [12,15,20,22,30]
media = sum(amostra) / len(amostra)

soma_quadrados = sum((x - media)** 2 for x in amostra)

variancia_amostral = soma_quadrados/ (len(amostra) -1)

print(f"A variância amostral desta amostra é: {variancia_amostral}")
