# Conversor de temperaturas: escreva um programa que converta uma temperatura digitada em ºC para ºF

c = float(input('Informe a temperatura em Cº: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}Cº, corresponde  a {}Fº!'.format(c, f))
