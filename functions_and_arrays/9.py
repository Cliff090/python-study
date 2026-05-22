def media(lista_notas):
    return sum(lista_notas) / len(lista_notas)

nomes = []

for i in range(4):  
    nome = input("Digite o nome do aluno: ")
    nomes.append(nome)
    notas_aluno = []  
    for j in range(3):#o J + 1 ta ai pra sair do zero vi isso dps
        nota = float(input(f"Digite a {j+1}ª nota do aluno {nome}: "))
        notas_aluno.append(nota)
    media_aluno = media(notas_aluno)
    print(f"A média do aluno {nome} é: {media_aluno:.2f}") #vi que o 2f limita quantas casas decimais apresenta