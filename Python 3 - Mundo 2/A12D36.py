# Desafio 036 - Escrever um programa que aprova o empréstimo bancário para a compra de uma casa. Perguntar o salário, valor da casa e em quantos anos será paga. A prestação não pode exceder 30% do salário.

# Solicita os dados ao usuário
valor_casa = float(input("Digite o valor da casa em reais: R$"))
salario_comprador = float(input("Qual o valor do seu salário em reais? R$"))
anos_pagamento = int(input("Em quantos anos você irá pagar a casa? "))

# Calcula o valor da prestação mensal
prestacao_mensal = valor_casa/(anos_pagamento * 12)

# Verifica se a prestação irá exceder 30% do salário do comprador e imprime uma mensagem formatada e colorida dizendo se o empréstimo foi aceito ou não
if (prestacao_mensal > 0.3 * salario_comprador):

    print("\033[1;31mEMPRÉSTIMO NEGADO\033[m")
    print(f"O valor da prestação de R${prestacao_mensal:.2f} excede 30% do seu salário.")

else:

    print("\033[1;32mEMPRÉSTIMO ACEITO!\033[m")
    print(f"Você irá pagar R${prestacao_mensal:.2f} por mês durante {anos_pagamento} anos.")
