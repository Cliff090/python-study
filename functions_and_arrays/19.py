def calcular_media(n1, n2,):
    media = (n1 + n2) / 2
    print(f"A média dos números é: {media:.2f}")

listadenums= []

for i in range(2):
    num= int(input("Digite um número: "))
    listadenums.append(num)
calcular_media(listadenums[0], listadenums[1])