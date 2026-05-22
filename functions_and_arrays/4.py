matriz = [
    [6, 2, 3],
    [8, 5, 7],
    [9, 4, 2]
]


for i in range(3):
    valor2= min(matriz[i])
    for j in range(3):
        valor= min(matriz[j])
print(f"O menor esta na linha {i} e ele é  {valor2}")