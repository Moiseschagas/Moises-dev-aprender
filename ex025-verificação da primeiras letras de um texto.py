# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"

cidade= input("Digite uma cidade: ").lower().strip().split()
print(cidade[0] == "santo")