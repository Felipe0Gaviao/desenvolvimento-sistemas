from os import system

def logo_senai():
    system("cls || clear")
    print("=== SENAI ===")

system("cls || clear")

notas = []

for i in range(3):
    notas.append(float(input("Digite uma nota: ")))

for i, nota in enumerate(notas, 1):
    print(f"Nota {i}: {nota}")

media = sum(notas)/len(notas)

print(media)