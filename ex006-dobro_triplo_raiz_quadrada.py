# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:


n = int(input('Digite um número: '))
print('O dobro do valor {} vale {}'.format(n, (n*2)))
print('O triplo do valor {} vale {}. \nA raiz quadrada {} vale {:.2f}.'.format(n, (n*3), n, (n**(1/2))))


