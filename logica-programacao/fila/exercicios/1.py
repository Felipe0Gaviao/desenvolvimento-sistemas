import os


os.system ("cls || clear")


limite_da_pilha = 25
fila = []






def adicionar():
    if len (fila) >= limite_da_pilha:
        print ("Limite atingido!")
    else:
        item = input("Digite o item que quer adicionar a pilha: ")
        fila.append (item)
        print (f"{item} foi cadastrado com sucesso!")
   


def verificar():
    if len (fila) == 0:
        print ("Não há itens na pilha!")
    else:
        print ("Há itens na pilha!")




def listar():
    if len (fila) == 0:
        print ("Não há itens na pilha")
    else:
        print ("Elementos da pilha: ")
        for i, item in enumerate(fila):
            print(f"{i + 1}: {item}")


def remover_primeiro_item():
    if len (fila) == 0:
        print ("Sua pilha ja está vazia!")
        return
   
    item_removido = fila.pop(0)
    print (f"{item_removido} foi removido da pilha!")




def remover_todos():
    if len (fila) == 0:
        print ("Sua pilha já está vazia")
    else:
        fila.clear()
        print ("Excluímos sua pilha!")
       


           
while True:
    print ("""\n Menu
    1- Adicionar um elemento
    2- Verificar se existe elementos na fila
    3- Listar os elementos da fila
    4- Remover primeiro elemento da fila
    5- Remover TODOS os elementos da fila
    6- Sair do Programa
    """)


    match input("Escolha uma opção: "):


        case "1":
            adicionar()
   
        case "2":
            verificar()
     
        case "3":
            listar()
   
        case "4":
            remover_primeiro_item()
   
        case "5":
            remover_todos()


        case "6":
            print("Saindo do Programa...")
            break
       
        case _:
            print ("Opção inválida!")

