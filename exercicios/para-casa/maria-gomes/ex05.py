numeros = [1, 2, 2, 3, 4, 4, 4, 5, 5]

contagem_principal = 0
numero_principal = 0
contagem_atual = 0
numero_atual = 0

numeros_ordenados = sorted(numeros)

for cada in numeros_ordenados:
    if cada == numero_atual:
        contagem_atual += 1
    else:
        if contagem_atual > contagem_principal:
            numero_principal = numero_atual
            contagem_principal = contagem_atual
        numero_atual = cada
        contagem_atual = 1

if contagem_atual > contagem_principal:
    numero_principal = numero_atual
    contagem_principal = contagem_atual

print(numero_principal)
