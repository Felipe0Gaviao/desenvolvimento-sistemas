import os

os.system("cls || clear")

n1 = int(input("Digite o Primeiro Número: "))
operador = input("Digite a Operação a ser Realizada: ")
n2 = int(input("Digite o Segundo Número: "))

if operador == "+":
    resultado = n1 + n2
elif operador == "-":
    resultado = n1 - n2
elif operador == "*":
    resultado = n1 * n2
elif operador == "/":
    resultado = n1 / n2
else:
    resultado = ""
    print("Operador Inválido")

print(f"{n1} {operador} {n2} = {resultado}")