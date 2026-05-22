def verificar_aprovação(media):
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado.")


listadenotas = []

for i in range (3):
    nota = float(input("Digite a nota do aluno: "))
    listadenotas.append(nota)
    media = sum(listadenotas) / len(listadenotas)
print(f"A média do aluno é: {media:.2f}")
verificar_aprovação(media)