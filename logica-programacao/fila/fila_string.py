import os

os.system("cls || clear")

fila = []

for _ in range(3):
    texto = input("Digite um número: ")
    fila.append(texto)
print("Fila: ", fila)

primeiro_elemento = fila.pop(0)
print("Primeiro Elemento: ", primeiro_elemento)
print("Fila: ", fila)