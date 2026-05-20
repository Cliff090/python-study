#Sintaxe

#lista = [
 #    [1, 2 ,3 ],
  #   [3, 5 , 4]
#]


#Estrutura de repetição pra print de valores matriz

#for linha in lista :
#    for valor in linha:
#        print(valor)

matriz= []


for i in range(3):
    linha=[]
    for j in range(3):
        num= int(input("insira um valor"))
        linha.append(num)
        print(f"entro na linha {j} da coluna {i}")
    matriz.append(linha)

print(matriz)


#diagonais principal

for i in range(3):
    print(matriz[i][i])