# Desafio 059 - Ler dois valores e mostrar um menu na tela: 1 somar, 2 multiplicar, 3 maior, 4 novos números e 5 sair do programa. Realizar a operação solicitada em cada caso.

# Solicita os valores de entrada ao usuário e mostra o menu de opções
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

menu = """\033[33m

        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR 
    \033[m
    """
print(menu)
option = int(input("Selecione uma opção: "))
print("")

# Verifica a opção escolhida e realiza a operação correspondente
while (option != 5):
    if (option == 1):
        resultado = valor1 + valor2
        print(f"\033[34mA soma entre {valor1} e {valor2} é igual a {resultado}\033[m")

    elif (option == 2):
        resultado = valor1 * valor2
        print(f"\033[34mO produto entre {valor1} e {valor2} é igual a {resultado}\033[m")

    elif (option == 3):
        if (valor1 > valor2):
            resultado = valor1
        else:
            resultado = valor2

        print(f"\033[34mEntre {valor1} e {valor2}, o maior número é o {resultado}\033[m")

    elif (option == 4):
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))

    print(menu)
    option = int(input("Selecione uma opção: "))
    print("")
    
print("\033[1;31m>>> FIM DO PROGRAMA <<<\033[m")
