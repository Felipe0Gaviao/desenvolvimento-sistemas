import os

os.system("cls || clear")


numero = int(input("Digite um número: "))

for i in range(1, 6):
    print(f"{numero} x {i} = {numero * i}")

for i in range(5):
    print(f"{numero} x {i + 1} = {numero * (i + 1)}")