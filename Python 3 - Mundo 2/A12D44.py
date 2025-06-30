# Desafio 044 - Elaborar um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e a condição de pagamento - à vista em dinheiro/cheque 10% de desconto; à vista cartão 5% de desconto; até 2x cartão preço normal e 3x ou mais 20% de juros

# Solicita o valor do produto e a forma de pagamento ao usuário
valor_produto = float(input("Digite o valor do produto: R$"))
print("""
      Qual será a forma de pagamento?
      1. À vista em dinheiro ou cheque - 10% de desconto
      2. À vista com cartão - 5% de desconto
      3. 2x sem juros com cartão
      4. 3x ou mais com cartão - 20% de juros
    """) 
forma_de_pagamento = int(input("Digite o número referente a opção: "))
   
# Verifica a forma de pagamento selecionada e calcula o valor final a ser pago, imprimindo uma mensagem com o resultado
if (forma_de_pagamento == 1):

    valor_final = (valor_produto - (valor_produto * 0.1))
    print(f"Você escolheu a forma de pagamento \033[1;33mÀ VISTA EM DINHEIRO OU CHEQUE\033[m. Total a pagar: \033[1;32mR${valor_final:.2f}\033[m")

elif (forma_de_pagamento == 2):

    valor_final = (valor_produto - (valor_produto * 0.05))
    print(f"Você escolheu a forma de pagamento \033[1;33mÀ VISTA COM CARTÃO\033[m. Total a pagar: \033[1;32mR${valor_final:.2f}\033[m")

elif (forma_de_pagamento == 3):

    valor_final = (valor_produto/2)
    print(f"Você escolheu a forma de pagamento \033[1;33m2X SEM JUROS NO CARTÃO\033[m. Total a pagar: \033[1;32mR${valor_final:.2f}\033[m")

elif (forma_de_pagamento == 4):

    parcelas = int(input("Em quantas parcelas deseja pagar? "))
    valor_final = (valor_produto + (valor_produto * 0.2))
    print(f"Você escolheu a forma de pagamento \033[1;33m{parcelas}X COM JUROS\033[m. Total a pagar: \033[1;32mR${valor_final:.2f}\033[m")

else:

    print("\033[1;31mFORMA DE PAGAMENTO INVÁLIDA\033[m")
