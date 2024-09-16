# Desafio 011 - Criar um programa que calcule a quantidade de tinta necessária para pintar uma parede. Dados: 1L de tinta pinta 2m²

# Recebe os valores da altura e do comprimento da parede (m)
comprimento = float(input("Digite o comprimento da parede, em metros(m): "))
altura = float(input("Digite a altura da parede, também em metros(m): "))

# Calcula a área da parede e a quantidade de tinta necessária
area = comprimento * altura
quantidade_tinta = area/2

# Imprime o resultado em L
print(f"\nA quantidade de tinta necessária para pintar uma parede de {area:.2f}m² são {quantidade_tinta:.2f}L ")