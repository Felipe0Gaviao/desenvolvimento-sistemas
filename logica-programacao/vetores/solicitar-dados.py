import os

os.system("cls || clear")

# notas = [2, 3, 4, 5]
notas = []

for _ in range(3):
    notas.append(float(input("Digite uma nota: ")))

for nota in notas:
    print(nota)