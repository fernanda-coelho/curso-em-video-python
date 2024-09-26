# Desafio 025 - Criar um programa que verifica se a pessoa tem "Silva" no nome

# Solicita o nome do usuário, remove os espaços no início e fim da string e converte todas as letras em minúsculo para garantinr que a comparação seja case-insensitive; também separa as palavras para evitar falso-positivos em nomes que se iniciam com 'silva'
nome = input("Digite o seu nome completo:\n>> ")
nome = nome.lower().strip().split()

# Verifica a presença da substring 'silva' na string nome com o operador in
print(f"\nPossui o sobrenome 'Silva'? \n>> {'silva' in nome}")
