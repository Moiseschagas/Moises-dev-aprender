# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Qual o salário do funcionário? R$ '))
novo = salario + (salario * 15 / 100)
print('O salario do funcionrio é R${:.2f} e com 15% de aumento ficará R${:.2f}'.format(salario, novo))
