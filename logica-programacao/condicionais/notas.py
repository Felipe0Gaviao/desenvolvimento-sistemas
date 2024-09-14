import os

os.system("cls || clear")

nota = int(input("Digite uma nota: "))

if nota >= 7:
    resultado = "Aprovado"
elif nota >=5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print(f"Resultado: {resultado}")