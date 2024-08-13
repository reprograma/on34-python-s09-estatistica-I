temperaturas = [32, 35, 23, 25, 28]

def calcular_media(numeros):
    soma = 0

    for cada in numeros:
        soma += cada

    resultado = soma / len(numeros)

    return round(resultado, 2)

def calcular_mediana(numeros):
    ordenados = sorted(numeros)
    resultado = 0

    if len(ordenados) % 2 == 0:
        indice1 = int((len(numeros) / 2) - 0.5)
        indice2 = int((len(numeros) / 2) + 0.5)
        metade = (ordenados[indice1] + ordenados[indice2]) / 2
        resultado = metade
    else:
        indice = int((len(numeros) / 2) - 0.5)
        resultado = ordenados[indice]

    return resultado

def calcular_moda(numeros):
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

    return numero_principal

print("--------RESULTADO--------")
print("Média: ", calcular_media(temperaturas))
print("Mediana: ", calcular_mediana(temperaturas))
print("Moda: ", calcular_moda(temperaturas))
