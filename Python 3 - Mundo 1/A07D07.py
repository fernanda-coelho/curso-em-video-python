# Desafio 07 - Criar um programa que lê duas notas e calcula a média do aluno

# Solicita as notas ao usuário
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

# Calcula a média
media = (nota1 + nota2)/2

# Imprime o valor da média do aluno com formatação de 2 casas decimais
print(f"A sua média escolar foi igual a {media:.2f}")
