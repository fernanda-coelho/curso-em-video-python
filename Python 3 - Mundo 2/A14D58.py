# Desafio 058 - Melhorar o jogo do desafio 028 onde o computador "pensa" em um número entre 0 e 10. O jogador deve tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Importa o método randint do módulo random para selecionar um número aleatório
from random import randint

# Gera um número aleatório entre 0 e 10 e armazena em uma variável
numero_aleatorio = randint(0, 10)
tentativas = 1

print("\033[1;35m=~"*30)
print("DESAFIO - Tente acertar o número escolhido pelo computador!")
print("=~"*30)
print("\033[m")

# Solicita um número inteiro ao usuário
numero_usuario = int(input("Digite um número inteiro entre 0 e 10: "))

# Verifica se o número digitado é o mesmo que o número aleatório. Se não for, solicita uma nova entrada até o usuário acertar o valor
if numero_aleatorio == numero_usuario:
    print("\033[32mPARABÉNS, VOCÊ VENCEU!!!! :D\033[m")

else:
    while (numero_usuario != numero_aleatorio): 
        print(f"\033[31mPoxa, não foi dessa vez!\033[m \n")
        numero_usuario = int(input("Tente novamente. Digite um número inteiro entre 0 a 10: "))
        tentativas += 1

        if numero_aleatorio == numero_usuario:
            print(f"\033[32mVOCÊ VENCEU!!!! :D \nNúmero de jogadas: {tentativas}\033[m")
