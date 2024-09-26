# Desafio 030 - Criar um programa que recebe um número inteiro e verifica se é par ou ímpar

# Solicita o número ao usuário
numero = int(input("Digite um número: \n>> "))

# Verifica se o número é par e imprime uma mensagem
if (numero % 2) == 0:

    print(f"O número {numero} é PAR!")

else:

    print(f"O número {numero} é ÍMPAR!")
