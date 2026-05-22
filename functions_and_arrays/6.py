def soma(a, b , c):
    return a + b + c


matriz= [
    [5,8,9],
    [6,2,3],
    [2,5,0]
]
ma= []
for i in range(3):
    valor = matriz[i][i]
    ma.append(valor)
print(f"A diagonal principal é {ma}")

resultado = soma(ma[0], ma[1], ma[2])
print(f"A soma da diagonal principal é {resultado}")