# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Crie um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.

from random import choice

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
print('O aluno escolhido Foi {}'.format(choice(lista)))