import os

os.system("cls || clear")

n1 = int(input("Digite o Primeiro Número: "))
operador = input("Digite a Operação a ser Realizada: ")
n2 = int(input("Digite o Segundo Número: "))

match operador:
    case "+":
        resultado = n1 + n2      
    case "-":
        resultado = n1 - n2
    case "*":
        resultado = n1 * n2
    case "/":
        resultado = n1 / n2
    case _:
        resultado = "Operador Inválido"

print(f"{resultado}")