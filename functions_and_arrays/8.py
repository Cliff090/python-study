def maiorqdez(a):
    if a >10:
        return 1
    else:
        return 0

matriz = [
    [80, 20, 1],
    [24, 5 , 0],
    [11, 2, 4]
]

contador= 0
for i in range(3):
    for j in range(3):
        valor = matriz[i][j]
        contador += maiorqdez(valor)

print(f"A quantidade de números maiores que dez é {contador}")