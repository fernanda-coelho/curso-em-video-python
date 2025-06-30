# Desafio 054 - Ler o ano de nascimento de 7 pessoas e mostrar quantas não atingiram a maioridade e quantas atingiram

# Importa a função date do módulo datetime para obter a data atual
from datetime import date

quantidade_maioridade = 0
quantidade_menoridade = 0

# Itera de 1 até 7 para solicitar o ano de nascimento do usuário e calcula sua idade
for cont in range(1,8):

    ano_nascimento = (int(input(f"Pessoa {cont} - Digite o seu ano de nascimento: ")))

    idade = ((date.today().year) - ano_nascimento)

    # Verifica se o usuário é maior de idade e incrementa o contador correspondente
    if (idade >= 18):

        quantidade_maioridade += 1

    else:

        quantidade_menoridade += 1

# Imprime os resultados
print(f"\n\033[36mNúmero de pessoas igual ou acima de 18 anos: {quantidade_maioridade}\033[m")
print(f"\033[36mNúmero de pessoas com menos de 18 anos: {quantidade_menoridade}\033[m")
