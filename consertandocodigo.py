import os
import sys
os. system('clear') 

i = 0
contador_pares = 0import os
os.system("clear || cls")

#Calculando vale transporte
def vale(salario):
    vale_transporte = str(input("Deseja vale transporte? (S/N) "))
    if vale_transporte.lower() == 's':
        salario = salario - (salario * 6/100)
    else:
        salario = salario
        
    return salario
#Calculando desconto do inss

def inss(salario,salario_transporte):
    if salario <= 1100:
        valor = salario_transporte - (salario*7.5/100)
        
    elif salario >=1100.01 and salario <=2203.48:
        valor = salario_transporte - (salario*9/100)
        
    elif salario >=2203.49 and salario <=3305.22:
        valor = salario_transporte - (salario*12/100)
    
    elif salario >=3305.22 and salario <=6098:
        valor = salario_transporte - (salario*14/100)
    elif salario > 6099:
        valor = salario_transporte - 854.36
    return valor
#Dependentes

def dependentes():
    dependente_quant=int(input("Quantidade de dependentes: "))
    if dependente_quant >=1:
        dependente =189 * dependente_quant
    else:
        dependente = 0
    return dependente
#Calculando desconto irrf

def irrf(salario,salario_inss):
    
    if salario >=2259.20 and salario <=2826.65:
        resultado = salario_inss - (salario*7.5/100)
        
    elif salario >=2826.65 and  salario <=3751.05:
        resultado = salario_inss - (salario*15/100)
        
        
    elif salario >=3751.05 and  salario <=4664.68:
        resultado = salario_inss - (salario*22.5/100)
        
    elif salario >=4664.69:
        resultado = salario_inss - (salario*27.5/100)
        
    if desconto_dependente >= resultado:
        resultado = salario_inss
    
    return resultado
    
#matricula = int(input("Digite sua matricula: "))
#senha = int(input("Digite sua senha: "))
salario = int(input("Digite seu salario base: " ))

salario_transporte = vale(salario)
salario_inss = inss(salario,salario_transporte)
desconto_dependente = dependentes()
salario_irrf = irrf(salario,salario_inss)

print("Valor inss: ",salario_inss)
print("Valor irff: ",salario_irrf)
print("Valor inss: ",salario_inss)
print("Dep: ",desconto_dependente)
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