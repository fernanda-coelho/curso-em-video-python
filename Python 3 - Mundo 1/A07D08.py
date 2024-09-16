# Desafio 08 - Converter o número recebido em metros para centímetro e milímetro

# Solicita o valor em metros ao usuário
num = float(input("Digite a distância em metros (m): "))

# Calcula o valor em centímetros e milímetros
num_centimetro = num * 100
num_milimetro = num * 1000

# Imprime os resultados da conversão
print(f"{num} metros equivalem a {num_centimetro} centímetros e {num_milimetro} milímetros")
