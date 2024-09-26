# Desafio 027 - Ler nome e mostrar o primeiro e último nome separadamente

# Solicita o nome completo do usuário, remove os espaços no início e fim da string, coloca a primeira letra de cada palavra em maiúsculo com o método title e divide a string em uma lista de palavras com o método split 
nome = input("Digite o seu nome completo \n>> ").strip().title().split()

# Imprime o primeiro nome do usuário
print(f"Primeiro nome: {nome[0]}")

# Imprime o último nome do usuário
print(f"Último nome: {nome[-1]}")
