def verificar_idade(idade):
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

valor = int(input("Digite sua idade: "))
verificar_idade(valor)