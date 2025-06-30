# Desafio 41 - Ler o ano de nascimento de um atleta e mostrar sua categoria de acordo com a idade - até 9 anos mirim, até 14 infantil, até 19 junior, até 20 sênior e acima master

# Importa a função date do módulo datetime para trabalhar com datas
from datetime import date

# Solicita o ano de nacimento do usuário
ano_nascimento = int(input("Digite o ano que você nasceu: "))

# Calcula a idade do usuário a partir da data atual e o ano de nascimento dele
idade = (date.today().year - ano_nascimento)

# Verifica a categoria do atleta de acordo com a idade e imprime uma mensagem colorida no terminal
if (idade <= 9):

    print("\033[1;33mATLETA MIRIM\033[m")


elif (idade <= 14):

    print("\033[1;34mATLETA INFANTIL\033[m")


elif (idade <= 19):

    print("\033[1;35mATLETA JÚNIOR\033[m")


elif (idade <= 20):

    print("\033[1;36mATLETA SÊNIOR\033[m")


else:

    print("\033[1;32mATLETA MASTER\033[m")
