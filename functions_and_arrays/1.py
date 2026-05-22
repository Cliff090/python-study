matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input("Informe o valor: "))
        linha.append(valor)
    matriz.append(linha)
print(matriz)