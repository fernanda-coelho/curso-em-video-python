# Desafio 031 - Criar um programa que calcula o preço da passagem de uma viagem, sabendo que até 200km são cobrados R$0,50/km e para viagens mais longas R$0,45

# Solicita a distância da viagem do usuário
distancia_viagem = float(input("Qual a distância da viagem, em km? \n >> "))

# Calcula o valor da passagem de acordo com a distância e imprime o resultado formatado em 2 casas decimais
if (distancia_viagem <= 200):

    valor_passagem = (distancia_viagem * 0.5)

    print(f"Para a distância de {distancia_viagem} o valor da passagem é igual a R${valor_passagem:.2f500}")

else:

    valor_passagem = (distancia_viagem * 0.45)

    print(f"Para a distância de {distancia_viagem} o valor da passagem é igual a R${valor_passagem:.2f}")
