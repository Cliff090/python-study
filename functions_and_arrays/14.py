def somar(a, b):
    return a + b


listadenums= []

for i in range(2):
    num= int(input("Digite um número: "))
    listadenums.append(num)

resultado = somar(listadenums[0], listadenums[1])
print(f"A soma dos números é: {resultado}")