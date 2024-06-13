import os
os.system("cls || clear")
def calculo(peso,altura):
    imc = peso/(altura*altura)
    return imc

def exibindo(imc):
    if imc>18:
        resultado = "Peso normal"
        return resultado
contador = 0
nomes = []
conta = 0
#Solicitando dados do usuário em loop
while True:
    os.system("cls || clear")
    contador= 1 + contador
    nome=input(f"Digite o nome do {contador}º usuário ou sair: ")

#condição para sair do loop
    if nome.lower() == 'sair':
        break
#
    peso=float(input("Digite seu peso: "))
    altura=float(input("Digite sua altura: "))
#
    nomes.append(nome)

    conta=calculo(peso,altura)

#Exibindo resultados
for i in range (len (nomes)):
    print("Usuário: ",nomes[i])
    print("Exibindo: ",exibindo(conta))