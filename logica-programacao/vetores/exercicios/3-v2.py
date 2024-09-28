from os import system

def logo_senai():
    system("cls || clear")
    print("=== SENAI ===")

def calcular_media(notas: list):
    return sum(notas)/len(notas)

system("cls || clear")

notas = []

for i in range(3):
    logo_senai()
    notas.append(float(input("Digite uma nota: ")))


logo_senai()
for i, nota in enumerate(notas, 1):
    print(f"Nota {i}: {nota}")

media = calcular_media(notas)

print(media)