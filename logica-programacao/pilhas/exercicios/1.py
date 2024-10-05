import os

os.system("clear || cls")

tamanho_max = 20
pilha = [None] * tamanho_max  
topo = -1

def empilhar():
    global topo
    print("""Insira o nome do item que vai ser adicionado à pilha
Insira (S) para sair deste comando
---------------------------------------------""")
    item = input("-> ")

    if item.lower() == 's':
        print("Retornando para o menu")
        return

    if topo < tamanho_max - 1:
        topo += 1
        pilha[topo] = item
        print(f"{item} foi cadastrado com sucesso")
    else:
        print("Limite de itens cadastrados atingido!")

def desempilhar():
    global topo
    if topo == -1:
        print("A pilha está vazia!")
        return

    item_removido = pilha[topo] 
    topo -= 1  
    print(f"{item_removido} foi removido da pilha!")

def limpar():
    global topo
    if topo == -1:
        print("A lista já está vazia!")
    else:
        pilha.clear()
        topo = -1 
        print("A pilha foi limpa!")

def vazia():
    if topo == -1:
        print("A Pilha está vazia!")
    else:
        print("A Pilha NÃO está vazia!")

def listar():
    global topo
    if topo == -1:
        print("Lista vazia")
    else:
        print("Elementos na pilha:")
        for i in range(topo + 1):
            print(f"{i + 1} - {pilha[i]}")

while True:
    print("""
1 - Empilhar: Adiciona um item ao fim da pilha
2 - Desempilhar: Remove o último item da pilha
3 - Limpar: Remove todos os elementos da pilha
4 - Listar: Lista todos os elementos armazenados na pilha
5 - Vazia: Retorna Verdadeiro se a lista estiver vazia e Falso caso contrário
6 - Sair: Sair do programa
""")
    
    match input("Comando: "):
        case "1":
            empilhar()
        case "2":
            desempilhar()
        case "3":
            limpar()
        case "4":
            listar()
        case "5":
            vazia()
        case "6":
            print("Saindo do programa...")
            break
        case _:
            print("Comando inválido! Tente novamente.")