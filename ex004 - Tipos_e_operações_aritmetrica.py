n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1 // n2
ex = n1 ** n2
print('A soma {}, a multiplicação é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira {} e a potência {}'.format(di, ex))
