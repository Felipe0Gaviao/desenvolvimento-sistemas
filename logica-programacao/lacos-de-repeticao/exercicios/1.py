import os

os.system("cls || clear")


numero = int(input("Digite um número: "))

for i in range(1, 10):
    print(f"{numero} x {i} = {numero * i}")