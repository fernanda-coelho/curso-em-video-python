## Desafio 015 - Criar um programa que calcula o preço a pagar de um carro alugado, sabendo que a diária custa R$60,00 e o km rodado R$0.15

## Solicita o número de dias alugados e km rodados
dias = int(input("Por quantos dias o carro foi alugado?\n>> "))
quilometros_percorridos = float(input("Quantos km o carro percorreu?\n>> "))

## Calcula o preço a ser pago
valor = (dias * 60) + (quilometros_percorridos * 0.15)

## Imprime o valor
print(f"O valor a ser pago pelo cliente é R${valor:.2f}")