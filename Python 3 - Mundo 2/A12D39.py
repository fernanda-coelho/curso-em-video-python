# Desafio 039 - Ler o ano de nascimento do usuário e informar, de acordo com sua idade, sua situação no alistamento.
# Importa a função date do módulo datetime para obter a data atual
from datetime import date

# Solicita o ano de nascimento do usuário
ano_user = int(input("Digite o seu ano de nascimento: "))

# Calcula a idade do usuário a partir da data atual e a data de nascimento
idade = (date.today().year) - ano_user

# Verifica a situação de alistamento do usuário e imprime uma mensagem colorida no terminal de acordo com a situação - verde precisa se alistar, vermelho já se passaram anos do alistamento e amarelo faltam anos para o alistamento.
if (idade < 18):
    
    print(f"\033[1;33m>> Faltam {18-idade} anos para você se alistar.\033[m")

elif (idade == 18):

    print("\033[1;32m>> Você precisa se alistar!\033[m")

else:

    print(f"\033[1;31m>> Já se passaram {idade - 18} anos do alistamento.\033[m")