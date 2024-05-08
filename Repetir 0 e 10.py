import os
os.system ("clear")
nota=-1
soma=0
while nota<0 or nota>10:
    for i in range(3):
        nota = int(input(f"Digite a {i+1}º nota:"))
        soma=int(soma+nota)
        if nota<0 or nota>10:
            print("Tente novamente")
            break
media=int(soma/3)
print(f"Media: {media}")