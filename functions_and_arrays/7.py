def eh_par(a):
    if a % 2 == 0:
     return 1
    else:
        return 0

matriz= [
    [5,8,9],
    [6,2,3],
    [2,5,0]
]
contador2= 0
for i in range(3):
    for j in range(3):
        valor = matriz[i][j]
        contador2 += eh_par(valor)

print(f"A quantidade de números pares é {contador2}")