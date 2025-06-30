# Desafio 045 - Crie um programa que faça o computador jogar jokenpô com você

# Importa a função choice do módulo random para selecionar um item de uma lista aleatóriamente e a função sleep do módulo time para imprimir mensagens após um determinado tempo
from random import choice
from time import sleep

# Seleciona um item aleatório para o computador e solicita a entrada da escolha do usuário
computador = choice(['pedra', 'papel', 'tesoura'])

jogador = input("\033[34mPedra, Papel ou Tesoura? \n >>  \033[m").lower().strip()

# Verifica se o jogador digitou uma entrada válida
if (jogador != 'pedra') and (jogador != 'papel') and (jogador != 'tesoura'):

    print ("JOGADA INVÁLIDA") 


# Se o jogador fez uma jogada válida, verifica se o jogador ganhou, empatou ou perdeu para o computador e imprime uma mensagem
else:

    print("\033[1;33m\nJO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PÔ!!!\033[m\n")
    sleep(1)
    print(f"\033[1;35mVocê:\033[m {jogador} \n\033[1;36mComputador:\033[m {computador}\n")

    if (jogador == computador):
        
        print("\033[1;34mEMPATE!\033[m") 


    elif (jogador == 'pedra') and (computador == 'tesoura') or (jogador == 'papel') and (computador == 'pedra') or (jogador == 'tesoura') and (computador == 'papel'):
    
        print("\033[1;32mVOCÊ GANHOU!\033[m")


    else:

        print("\033[1;31mVOCÊ PERDEU!\033[m")
