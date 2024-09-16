# Desafio 013 - Calcular o novo salário de um funcionário que receberá 15% de aumento

# Solicita o valor do salário atual
salario = float(input("Digite o valor atual do seu salário: R$"))

# Calcula o novo salário com acréscimo de 15%
novo_salario = salario + (0.15 * salario)

# Imprime o valor do novo salário
print(f"O novo salário do funcionário será de R${novo_salario:.2f}")