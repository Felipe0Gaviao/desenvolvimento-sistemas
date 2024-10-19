import os

os.system("cls || clear")

fila = []

for i in range(3):
    num = int(input("Digite um número: "))
    fila.append(num)
print("Fila: ", fila)

primeiro_elemento = fila.pop(0)
print("Primeiro Elemento: ", primeiro_elemento)
print("Fila: ", fila)