from os import system

system("cls || clear")

nomes = []

for i in range(4):
    nomes.append(input(f"Digite o {i+1}° nome: "))

for nome in nomes:
    print(nome)