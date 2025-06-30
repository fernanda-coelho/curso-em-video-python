# Desafio 036 - Converter um número inteiro para uma base de escolha do usuário: binário, octal ou hexadecimal.

# Solicita o número ao usuário e qual a base de conversão
numero = int(input("Digite um número inteiro para a conversão: "))
escolha = int(input("Você quer converter para qual base? Digite o número correspondente: \n>> 1 - BINÁRIO \n>> 2 - OCTAL \n>> 3 - HEXADECIMAL\n"))

# Verifica a escolha do usuário e converte o número para a base desejada com o uso das funções embutidas bin(), oct() e hex(), imprimindo o resultado formatado removendo os dois primeiros caracteres para obter apenas a representação da parte fracionária do número
if (escolha == 1):

    print(f"O número {numero} em \033[1;33mbinário\033[m é igual a {bin(numero)[2:]}")


elif (escolha == 2):
  
    print(f"O número {numero} em \033[1;32moctal\033[m é igual a {oct(numero)[2:]}")


elif (escolha == 3):

    print(f"O número {numero} em \033[1;35mhexadecimal\033[m é igual a {hex(numero)[2:]}")


else: 

    print("\033[1;31mERRO!\033[m Opção inexistente. Escolha uma opção válida.")
