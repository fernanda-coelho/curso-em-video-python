# Desafio 40 - Calcular a média do aluno a partir de duas notas e mostrar se foi aprovado (>=7), reprovado (<5) ou está de recuperação (>=5 e <7)

# Solicita as notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média do usuário
media = (nota1 + nota2) / 2

# Verifica o status do usuário de acordo com a nota e imprime uma mensagem colorida no terminal - verde para aprovação, vermelho para reprovação e amarelo para recuperação
if (media < 5):

    print(f"\033[1;31m>> Você foi REPROVADO. Sua média foi igual a {media:.2f}\033[m")


elif (7 > media >=5):

    print(f"\033[1;33m>> Você está de RECUPERAÇÃO. Sua média foi igual a {media:.2f}\033[m")


else:

    print(f"\033[1;32mParabéns, você foi APROVADO!! Sua média foi igual a {media:.2f}\033[m")
