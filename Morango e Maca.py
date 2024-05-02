import os
os.system("clear")


Qmorango=float(input("Digite a quantidade de morangos: "))
if Qmorango<=5:
    precomorango=float(2.50)

elif Qmorango>5:
    precomorango=2.20

totalmorango=float(precomorango*Qmorango)

Qmacas=float(input("Digite a quantidade de maçãs: "))
if Qmacas<=5:
    precomacas=float(1.80)

elif Qmacas>5:
    precomacas=1.50

totalmacas=float(precomacas*Qmacas)
total=float(totalmacas+totalmorango)
kilostotal=float(Qmorango+Qmacas)

if total>25 or kilostotal>8:
    total=total-(0.10*total)
    print(f"Total: {total}")

else :
    print(f"Total: {total}")
