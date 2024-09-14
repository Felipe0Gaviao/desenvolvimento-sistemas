import os

os.system("cls || clear")

nota = -1

nota = float(input("Digite uma nota: "))

while nota < 0.0:
    print(f"Nota não pode ser menor que 0")
    nota = float(input("Tente novamente: "))

print(f"Nota: {nota}")