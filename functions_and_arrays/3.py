matriz = [
    [1, 2, 3],
    [8, 5, 7],
    [9, 4, 2]
]

for i in range(3):
    valor2= max(matriz[i])
    for j in range(3):
        valor= max(matriz[j])
print(f"O maior esta na linha {i} e ele é  {valor2}")