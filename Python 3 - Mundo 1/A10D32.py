# Desafio 032 - Verificar se o ano digitado é bissexto

# importa o método datetime do módulo date para pegar o ano atual
from datetime import date

# Solicita o ano ao usuário
ano = int(input("Digite um ano ou coloque 0 para analisar o ano atual: \n >> "))

# Pega o ano atual da máquina se o usuário digitou '0'
if (ano == 0):

    ano = date.today().year

# Verifica se o ano é bissexto e imprime uma mensagem - para ser bissexto, um ano precisa ser divisível por 4, exceto se o ano for divisível por 100 (não é bissexto, a menos que também seja divisível por 400.
if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0:
    
    print(f"O ano de {ano} É BISSEXTO!")

else:

    print(f"O ano de {ano} NÃO É BISSEXTO!")
