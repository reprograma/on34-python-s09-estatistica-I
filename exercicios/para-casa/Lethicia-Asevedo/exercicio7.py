#Exercício 7: Análise de Vendas de Produtos

#Uma loja registrou o número de unidades vendidas de diferentes produtos ao
#longo de uma semana.
#Cada produto tem um código único e o número de unidades vendidas é
#registrado em uma lista. Escreva um programa em Python que:


#1. Calcule a média aritmética das unidades vendidas.

venda_mouse = int(input("Qntd de mouses vendidos da semana: "))
venda_teclado = int(input("Qntd de teclados vendidas na semana: "))
venda_mousepad = int(input("Qntd de mousepads vendidos na semana: "))
venda_webcam = int(input("Qntd de webcams vendidas na semana: "))
venda_monitor = int(input("Qntd de monitores vendidos na semana: "))

media = (venda_mouse+venda_monitor+venda_mousepad+venda_teclado+venda_webcam) / 5

print (f"A média de produtos vendidos na semana é: {media:.0f}")

#2. Encontre a mediana das unidades vendidas.
mediana = [venda_mouse,venda_monitor,venda_mousepad,venda_teclado,venda_webcam]
mediana.sort()
tamanho = len(mediana)
mediana = mediana[tamanho //2]
print(f"A mediana das notas inseridas é: {mediana}")

#3. Identifique o produto mais vendido (moda).

vendas = [venda_mouse,venda_monitor,venda_mousepad,venda_teclado,venda_webcam]
frequencia = {}
for num in vendas:
    if num in frequencia:
        frequencia[num]+=1
    else:
        frequencia[num]=1

max_frequencia = max(frequencia.values())

produtos_mais_vendidos = [num for num, freq in frequencia.items() if freq == max_frequencia]

# Mapeamento de vendas para nomes e códigos dos produtos
produtos = {
    venda_mouse: ("Mouse", "prod1_mouse"),
    venda_teclado: ("Teclado", "prod2_teclado"),
    venda_mousepad: ("Mousepad", "prod3_mousepad"),
    venda_webcam: ("Webcam", "prod4_webcam"),
    venda_monitor: ("Monitor", "prod5_monitor")
}

for produto in produtos_mais_vendidos:
    nome, codigo = produtos[produto]
    print(f"A moda ou produto mais vendido foi: {nome} (Código: {codigo})")

