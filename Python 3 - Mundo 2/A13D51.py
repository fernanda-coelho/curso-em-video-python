# Desafio 051 - Desenvolver um programa que leia o primeiro termo e a razão de uma PA. No final mostrar os 10 primeiros termos dessa progressão.

# Solicita os dados ao usuário
termo1 = float(input("Digite o primeiro termo da progressão aritmética: "))
razao = float(input("Digite a razão da PA: "))
termo = termo1

print("")

# Itera de 1 a 10
for cont in range(1, 11):

    # Imprime o termo da PA e calcula o próximo termo
    print(f"{cont}° termo: {termo}")
    termo += razao

print("\033[31mFIM\033[m")
