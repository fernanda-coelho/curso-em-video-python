# Desafio 060 - Ler um número e mostrar o seu fatorial

# Inicializa a variável que armazenará o resultado e solicita ao usuário um número inteiro
resultado = 1
numero = int(input("\033[33mDigite um número: \033[m"))

# Executa um loop para realizar a multiplicação dos números, encontra o fatorial e retorna o resultado 
while (numero > 0):
    print (f"{numero} x" if (numero > 1) else f"{numero} =" , end=' ')
    resultado *= numero 
    numero -= 1

print(resultado)
