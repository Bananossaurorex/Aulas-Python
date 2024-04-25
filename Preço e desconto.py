import os
os.system("clear")

quantidade=int(input("Digite a quantidade: "))
preçouni=float(input("Digite o preço do produto: "))

total=float(quantidade*preçouni)

if quantidade<=5:
    desconto=float(0.02)

elif quantidade>5 and quantidade<=10:
    desconto=float(0.03)

elif quantidade>10:
    desconto=float(0.05)

totalapagar= total-(total*desconto)
print(f"Total a pagar: {totalapagar}")