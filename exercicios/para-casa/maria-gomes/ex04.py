numeros = [1, 3, 4, 2, 5]

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

print(resultado)