import os

os.system("clear || cls")

pilha = []


def empilhar():
    print("""Insira o nome do item que vai ser adicionado a pilha
Insira (S) para sair deste comando
---------------------------------------------""")
    item = input("")


    while True:
        if item == "":
            print("Item não pode ser vazio")
            item = input("Insira o nome novamente: ")
        elif item.lower() == "s":
            print("Retornando para o menu")
            break
        else:
            pilha.append(item)
            break
    
empilhar()