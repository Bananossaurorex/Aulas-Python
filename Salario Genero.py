import os
os.system ("clear")

opcao=1
mulherica=0
while opcao!=0:
    print("1- Adicionar pessoa")
    print("2- Exbir resultados")
    print("0- Parar programa")
    opcao=int(input("Escolha uma opção: "))
    match (opcao):
        case 1:
            genero=str(input("Digite o genero (M/F): "))
            salario=float(input("Digite o salario: "))
            idade=int(input("Digite sua idade: "))
            if genero=="m" and salario>=5000:
                mulherica=mulherica+1
            os.system("clear")
        case 2:
            print(f"Seu genero: {genero}")
            print(f"Seu salario: {salario}")
            print(f"Sua idade: {idade}")
            print(f"Quantidade de mulheres ricas: {mulherica}")
            break

        