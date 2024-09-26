# Desafio 033 - Ler três números e mostrar qual é o maior e o menor

# Solicita o número ao usuário e define o primeiro número como o maior até o momento
numero = float(input("Digite o primeiro número: "))

maior = numero

# Solicita o segundo número ao usuário
numero = float(input("Digite o segundo número: "))

# Verifica se o segundo número é maior que o primeiro
if (numero > maior):

    menor = maior
    maior = numero

else:

    menor = numero

# Solicita o terceiro número ao usuário
numero = float(input("Digite o terceiro número: "))

# Verifica se o terceiro número é maior que o número definido como o maior
if (numero > maior):

    maior = numero

# Caso o terceiro número não seja maior que o número definido como maior, verifica se ele é menor que o número definido como menor número
elif (numero < menor):

    menor = numero

# Imprime os resultados
print(f"Maior Número: {maior}")
print(f"Menor Número: {menor}")
