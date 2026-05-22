matriz= []

for i in range(2):
    linha = []
    for j in range(3):
        valor = int(input("Digite o valor á ser adicionado:"))
        linha.append(valor)
    matriz.append(linha)
print(matriz)