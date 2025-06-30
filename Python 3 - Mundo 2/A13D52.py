# Desafio 052 - Ler um número inteiro e verificar se é primo ou não

# Solicita um número ao usuário
numero = int(input("Digite um número: "))

divisoes = 0

# Itera de número até 1, verificando se o número é divisível por cada número
for cont in range(1, numero+1):

    if(numero % cont == 0):
    
        divisoes += 1
        print(f"\033[32m{cont}\033[m", end=" ")

    else:
        print(f"\033[31m{cont}\033[m", end=" ")

# Se o número for divisível apenas por 1 e ele mesmo, imprime a mensagem que é primo, caso contrário, que não é primo.
if (divisoes == 2):
    
    print(f"\n\033[36m>> O número {numero} é primo\033[m")


else:
    
    print(f"\033[36m>> O número {numero} não é primo\033[m")
