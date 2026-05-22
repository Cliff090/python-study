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