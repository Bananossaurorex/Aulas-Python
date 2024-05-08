import os
os.system ("clear")
contador=0
soma=0
media=0
for i in range (1,4):
    contador =int(contador +1)
    nota=int(input(f"Digite sua {i}º nota: "))
    soma+=nota
media=int(soma/contador)
print(f"Media: {media}")
if media>=7:
    print("Aprovado")
elif media>=5 and media<7:
    print("Recuperação")
if media<5:
    print("Reprovado")