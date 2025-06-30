# Desafio 061 - Ler o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

# Solicita os valores ao usuário
razao = int(input("Digite a razão da Progressão Aritmética: "))
numero = int(input("Primeiro termo: "))

cont = 0

# Realiza um loop para calcular os primeiros 10 termos da PA e imprime o resultado
while(cont != 10):
    print(f"\033[34m{numero} →\033[m", end=' ')

    numero += razao
    cont += 1

print(f"\033[31mFIM\033[m")
