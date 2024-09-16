# Desafio 020 - Criar um programa que sorteie a ordem de apresentação de 4 alunos

# Importa a função shuffle do módulo random, responsável por reorganizar a ordem dos itens de uma sequência
from random import shuffle

# Solicita o nome dos alunos ao usuário
aluno1 = input("Digite o nome do 1° aluno: ")
aluno2 = input("Digite o nome do 2° aluno: ")
aluno3 = input("Digite o nome do 3° aluno: ")
aluno4 = input("Digite o nome do 4° aluno: ")

# Armazena os nomes dos alunos em uma lista e reorganiza a ordem
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista_alunos)

# Imprime a ordem de apresentação dos alunos
print(f"A ordem de apresentação será: {lista_alunos}")
