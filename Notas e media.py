import os
os.system("clear")

nome=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))
nota1=int(input("Digite sua primeira nota: "))
nota2=int(input("Digite sua segunda nota: "))

media=float((nota1+nota2)/2)
os.system("clear")

if media<7:
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Media: {media}")
    print(f"Você está reprovado")

else:
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Media: {media}")
    print(f"Você está aprovado")

