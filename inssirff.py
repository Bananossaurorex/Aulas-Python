import os
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
        valor = (salario*7.5/100)
        
    elif salario >=1100.01 and salario <=2203.48:
        valor = (salario*9/100)
        
    elif salario >=2203.49 and salario <=3305.22:
        valor = (salario*12/100)
    
    elif salario >=3305.22 and salario <=6098:
        valor = (salario*14/100)
    elif salario > 6099:
        valor = salario_transporte - 854.36
    return valor
#Dependentes

def dependentes():
    if dependente_quant > 0:
        dependente =189.59 * dependente_quant
    else:
        dependente = 0
    return dependente
    
def saude():
    plano=str(input("Deseja plano de saúde? "))
    if plano.lower() == 's':
        total_saude = (dependente_quant*150) + 150
    else:
        total_saude = dependente_quant*150
    return total_saude
    
#Calculando desconto irrf

def irrf(salario,salario_inss,desconto_dependente):
    
    if salario >=2259.20 and salario <=2826.65:
        resultado = (salario*7.5/100)
        
    elif salario >=2826.65 and  salario <=3751.05:
        resultado = (salario*15/100)
        
    elif salario >=3751.05 and  salario <=4664.68:
        resultado = (salario*22.5/100)
        
    elif salario >=4664.69:
        resultado = (salario*27.5/100)
        
    resultado_final = resultado - desconto_dependente
    if desconto_dependente > resultado:
        resultado_final = 0
    return resultado_final
    
def refeicao():
    resultadoref=str(input("Deseja salario refeição? "))
    if resultadoref.lower() == 's':
        resultadoref=500-(20/100*500)
    return resultadoref
    
matricula = int(input("Digite sua matricula: "))
senha = int(input("Digite sua senha: "))
salario = int(input("Digite seu salario base: " ))
dependente_quant =int(input("Quantidade de dependentes: "))

salario_transporte = vale(salario)
desconto_dependente = dependentes()
salario_inss = inss(salario,salario_transporte)
salario_irrf = irrf(salario,salario_inss,desconto_dependente)
salario_refeicao = refeicao()
plano_saude = saude()
salario_final = salario_transporte - salario_refeicao - salario_irrf - salario_inss - plano_saude 

os.system ("clear || cls")
print("Valor base: R$",salario)
print("Valor com vale transporte: R$",salario_transporte)
print("Valor inss: R$",salario_inss)
print("Valor irRf: R$",salario_irrf)
print("Valor do beneficio: R$",salario_refeicao)
print("Dedução por dependente: ",desconto_dependente)
print("Plano de saúde: ",plano_saude)
print("Valor final: R$",round(salario_final,2))