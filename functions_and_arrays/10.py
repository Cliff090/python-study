def somadalinha(linha):
    soma= 0
    for i in linha:
        soma+=i
    return soma


matriz= [
[1,2,3],
[4,5,6],
[7,8,9]]





for linha in matriz:
    valor = (somadalinha(linha))
    for i in range(3):
        lines= []
        lines.append(valor)
    print(f" o valor da soma na linha {matriz.index(linha)+1} é {lines}")
