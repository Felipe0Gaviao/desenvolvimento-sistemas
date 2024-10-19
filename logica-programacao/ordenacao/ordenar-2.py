import random, os

os.system('cls || clear')

atrizes = ['Adriana Prado', 'Bárbara Borges', 'Camila Quiroz', 'Danielle Winits', 'Fernanda Paes Leme', 'Helena Ranaldi', 'Paola de Oliveira', 'Raquel Nunes', 'Viola Davis']

random.shuffle(atrizes)
print(atrizes)

atrizes.sort()
print(atrizes)

atrizes.sort(reverse=True)
print(atrizes)