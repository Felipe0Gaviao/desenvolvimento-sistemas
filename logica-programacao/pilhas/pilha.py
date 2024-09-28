import os

os.system("cls || clear")

lista = []

while True:
    print("""\nMenu de opções
    1 - Adicionar um livro a lista
    2 - Visualizar lista de livros
    3 - Remover um livro da lista
    4 - Sair do programa""")

    x = int(input("Digite a ação tomada: \n"))

    match x:

        case 1:
            livro = input("\nDigite o nome do livro a ser adicionado: ")
            if livro == '':
                print("\nLivro precisa ter um nome")
                print("Tente novamente")
                continue
            else:
                print(f"\nAdicionando livro: {livro}")
                lista.append(livro)
                print('Livro adicionado')

        case 2:
            if not lista:
                print("\nA lista de livros está vazia")
            else:
                for i, livro in enumerate(lista, start=1):
                    print(f"{i} - {livro}")

        case 3:
            if not lista:
                print("\nA lista de livros está vazia")
            else:
                print("\nPor favor selecione um livro pelo número ao lado do nome")
                for i, livro in enumerate(lista, start=1):
                    print(f"{i} - {livro}")
                
                id_livro = int(input("\nRemover livro com id: "))
                
                if len(lista) < id_livro or id_livro < len(lista):
                    print("\nId digitado está fora da área da lista")
                else:
                    print(f"\nRemovendo livro: {lista[id_livro - 1]}")
                    lista.pop(id_livro - 1)
                    print("Livro Removido!")

        case 4:
            print("\nSaindo do programa...")
            break