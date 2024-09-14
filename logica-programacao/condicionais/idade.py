import os

os.system("cls || clear")

resposta: str

idade = int(input("Digite sua idade: "))

if idade < 18:
    resposta = "Menoridade"
else:
    resposta = "Maioridade"

print(f"Resultado: {resposta}")

print(f"{' FIM ':=^11}")