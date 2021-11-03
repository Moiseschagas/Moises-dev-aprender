# Crie um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = "Tertuliano da Silva Moraes Menezes Bueno de Andrada"
nome = nome.split()
print(nome)
print("Primeiro = {}".format(nome[0]))
print("Último = {}".format(nome[-1]))