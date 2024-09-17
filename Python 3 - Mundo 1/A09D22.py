# Desafio 022 - Criar um programa que lê o nome do usuário e mostra com todas as letras maiúsculas, todas as letras minúsculas, letras ao todo (sem espaços) e quantas letras no primeiro nome.

# Solicita o nome do usuário
nome = input("Digite o seu nome: ")

# Imprime o nome em maiúsculas e minúsculas
print(f"Nome em maiúsculas: {nome.upper()}")
print(f"Nome em minúsculas: {nome.lower()}")

# Remove os espaços e imprime a quantidade de letras do nome completo
letras = nome.strip()
print(f"Letras ao todo: {len(letras) - letras.count(' ')}")

# Separa a string e imprime a quantidade de letras do primeiro nome apenas
letras1 = nome.split()
print(f"Letras no primeiro nome: {len(letras1[0])}")
