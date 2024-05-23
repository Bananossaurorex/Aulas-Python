import os
import sys
os. system('clear') 

i = 0
contador_pares = 0
contador_impares = 0
positivos = 0
negativos = 0
numeros = []

for i in range (5):
    num=int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Calculando Pares e Impares
if num % 2 == 0:
    contador_pares += 1
else:
    contador_impares+=1
# Calculando Positivos e negativos
if num > 0:
    positivos+=1
else:
    negativos+=1
# Exibindo
print(f"Quantidade de Pares: {contador_pares}")