# Desafio 049 - Mostrar a tabuada de um número que o usuário escolher, utilizando o laço for

# Solicita o número ao usuário
numero = int(input("Qual número você deseja saber a tabuada? "))

print(f"\n\033[36mTABUADA DO {numero}\n\033[m")

# Itera de 1 até 10 e realiza a multiplicação, imprimindo o resultado
for cont in range (1, 11):

    resultado = (numero * cont)
    print(f"{numero} * {cont} = {resultado}")
