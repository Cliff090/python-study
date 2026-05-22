def subtrair(a, b):
    return a - b


listadenums= []

for i in range(2):
    num= int(input("Digite um número: "))
    listadenums.append(num)

resultado = subtrair(listadenums[0], listadenums[1])
print(f"A subtração dos números é: {resultado}")