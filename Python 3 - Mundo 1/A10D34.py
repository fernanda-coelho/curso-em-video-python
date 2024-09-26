# Desafio 034 - Verificar o salário de um funcionário e calcular o valor do seu aumento. Salários maiores que R$1200,00 recebem aumento de 10% e salários iguais ou inferiores recebem aumento de 15%.

# Solicita o salário ao usuário
salario = float(input("Digite o seu salário: \n>> R$"))

# Verifica o valor do salário para aplicar o acréscimo correspondente
if (salario > 1200):

    salario_novo = (salario * 0.1) + salario

else:

    salario_novo = (salario * 0.15) + salario

# Imprime o valor do novo salário
print(f"O seu novo salário será de R${salario_novo:.2f}")
