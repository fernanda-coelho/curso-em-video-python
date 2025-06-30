# Desafio 046 - Mostrar uma contagem regressiva de 10 até 0 com uma pausa de 1 segundo entre eles

# Importa a função sleep do módulo time para a pausa
from time import sleep

print("\033[33m>> C O N T A G E M   R E G R E S S I V A <<\033[m")

# Realiza a contagem regressiva e imprime com pausa de 1 segundo
# O loop for itera de 10 até 0, decrementando de 1 em 1 a cada iteração
for contagem in range(10, -1, -1):

    print(contagem)
    sleep(1)

print("\033[31mFIM\033[m")
