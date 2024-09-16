# Desafio 012 - Calcular o novo preço de um produto com desconto de 5%

# Solicita o valor original do produto
preco = float(input("Digite o valor do produto: R$"))

# Calcula o novo preço com desconto de 5%
novo_preco = preco - (0.05 * preco)

# Imprime o novo valor do produto
print(f"O produto de R${preco:.2f} com 5% de desconto custará R${novo_preco:.2f}")
