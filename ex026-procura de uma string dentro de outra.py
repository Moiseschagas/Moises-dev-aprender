# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = str(input("Digite seu nome: "))
nome = nome.lower().strip().split()
print("silva" in nome)