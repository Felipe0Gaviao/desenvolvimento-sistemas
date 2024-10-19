lista = []

while True:
    match input('''
          1 - Cadastrar novo item
          2 - Listar
          3 - Listar Crescente
          4 - Listar Decrescente
          5 - Embaralhar
          6 - Sair
'''):
        case '1':
            lista.append(input('Novo item:'))
        case '2':
            print(lista, sep='\n')
        case '3':
            print(sorted(lista))