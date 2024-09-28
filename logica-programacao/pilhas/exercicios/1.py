import os

os.system("clear || cls")

pilha = []


def empilhar():
    print("""Insira o nome do item que vai ser adicionado a pilha
Insira (S) para sair deste comando
---------------------------------------------""")
    item = input("-> ")


    while True:
        if item == "":
            print("Item não pode ser vazio")
            item = input("Insira o nome novamente: ")
        elif item.lower() == "s":
            print("Retornando para o menu")
            break
        else:
            pilha.append(item)
            print(pilha)
            item = input("Adicione mais um item ou (s)air programa: ")

while True:
    print("""
Comandos:
1 - Empilhar: Adiciona um item ao fim da pilha
2 - Desempilhar: Remove o item ultimo item da pilha
3 - Limpar: Remove todos os elementos da pilha
4 - Listar: Lista todos os elementos armazenados na pilha
5 - Vazia: Retorna Verdadeiro se a lista estiver vazia e Falso caso contrário
6 - Sair: Sair do programa
""")
    comando = int(input("Comando: "))

    match comando:
        case 1:
            empilhar()
        case 2:
            desempilhar()
        case 3:
            limpar()
        case 4:
            listar()
        case 5:
            vazia()
        case 6:
            print("Saindo do programa...")
            break