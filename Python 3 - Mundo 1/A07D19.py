# Desafio 019 - Sortear um nome de aluno dentre os 4 nomes recebidos

# Importa a função choice do módulo random, responsável por retornar um elemento aleatório de uma sequência
from random import choice

# Solicita o nome dos alunos ao usuário
nome1 = input("Digite o nome do 1° aluno: ")
nome2 = input("Digite o nome do 2° aluno: ")
nome3 = input("Digite o nome do 3° aluno: ")
nome4 = input("Digite o nome do 4° aluno: ")

# Armazena o nome dos alunos em uma lista e retorna um nome aleatório da lista de alunos
lista_alunos = [nome1, nome2, nome3, nome4]
aluno = choice(lista_alunos)

# Imprime o nome do aluno selecionado aleatoriamente
print(f"O aluno escolhido foi {aluno}")
