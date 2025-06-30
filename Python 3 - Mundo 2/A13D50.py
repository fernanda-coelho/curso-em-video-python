# Desafio 050 - Ler seis números inteiros e mostrar a soma apenas dos pares, desconsiderar os ímpares

soma = 0

# Itera de 1 até 6
for cont in range(1, 7):

    numero = int(input(f"\033[33mDigite o {cont}° número: \033[m"))

    # Verifica se o número é par e em caso positivo, realiza a soma
    if (numero % 2 == 0):

        soma += numero

# Imprime o resultado da soma dos números pares
print(f"\nA soma entre os números pares é igual a \033[35m{soma}\033[m")
