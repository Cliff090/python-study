#Função principal é a repetição de comandos "poupa linha " 
#sintaxe


#def nome_da_função():
      #comandos 


def abilolado():
    print("hje tem algo")


#chamando sua função
abilolado()

#com parametro
#apenas printa e não salva o valor 
def junior(nome):
    print("seu nome é ", nome)

names = input("digite meu fih: ")
junior(names)



#Jeito certo com return para armazenar os valorems e não apenas mostrar na tela 

def somar(a, b):
    resultado= a+b
    return resultado 

final= somar(4,2)
outro= final+1
print(outro)

# Função com parametro para a verificação de se um numero é par ou impar 
def imapar(a):
    if a%2 ==0:
        print("Par")
    else:
        print("impar")

imbaba= int(input("Digite tua numeração: "))
imapar(imbaba)
