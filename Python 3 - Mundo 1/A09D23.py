# Desafio 023 - Ler um número de 0 a 9999 e mostrar cada um dos dígitos separados

# Solicita um número ao usuário
numero = int(input("Digite um número de 0 a 9999\n>> "))

# Separa cada os dígitos usando módulo e divisão inteira para pegar apenas o último e armazena em variáveis
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

# Imprime os resultados da separação
print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")
