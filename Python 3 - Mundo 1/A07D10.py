# Desafio 010 - Criar um programa que permite o usuário descobrir quantos dólares pode comprar, considerando 1US$ = R$5,55

# Recebe o valor em reais
reais = float(input("Digite o valor em reais: R$"))

# Converte o valor em reais para dólar
dolares = reais / 5.55

# Imprime o resultado
print(f"Com R${reais} você pode comprar US${dolares:.2f}!")
