import random, os

os.system('cls || clear')

lista = []

comandos = '''
1 - Cadastrar novo item
2 - Listar
3 - Listar Crescente
4 - Listar Decrescente
5 - Embaralhar
6 - Remover
7 - Sair
'''

def imprimir_em_ordem(lst):
    for i, item in enumerate(lst, start=1):
        print(f'{i}: {item}')

while True:
    match input(comandos):
        case '1':
            lista.append(input('Novo item:'))
        case '2':
            imprimir_em_ordem(lista)
        case '3':
            imprimir_em_ordem(sorted(lista))
        case '4':
            imprimir_em_ordem(sorted(lista, reverse=True))
        case '5':
            l = list(lista)
            random.shuffle(l)
            imprimir_em_ordem(l)
        case '6':
            numero = int(input('ID:'))

            if 0 > numero > len(lista):
                print('Número especificado está fora da lista')
                continue
            
            item = lista.pop(numero - 1)

            print(f'Item {item} removido da lista')
        case '7':
            print('Saindo do programa...')
            break
        case _:
            print('Comando inválido')