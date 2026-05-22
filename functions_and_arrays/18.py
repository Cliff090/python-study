def verificar_positivo(numero):
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")

valor = int(input("Digite um número: "))
verificar_positivo(valor)