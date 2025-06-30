# Desafio 048 - Calcular a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500

soma = 0

# Itera de 1 a 500, somente os pares
for cont in range(1, 501, 2):

    # Verifica se o número é múltiplo de três, e em caso positivo adiciona a soma
    if(cont % 3 == 0):

        soma += cont

# Imprime o valor da soma
print(f"A soma entre todos os números ímpares que são múltiplos de três entre o intervalo de 1 a 500 é igual a \033[35m{soma}\033[m")
