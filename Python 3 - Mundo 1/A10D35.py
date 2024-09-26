# Desafio 035 - Ler o comprimento de três retas e dizer se elas podem ou não formar um triângulo.

# Solicita o comprimento das retas ao usuário
lado1 = float(input("Digite o comprimento da primeira reta: "))
lado2 = float(input("Digite o comprimento da segunda reta: "))
lado3 = float(input("Digite o comprimento da terceira reta: "))

# Verifica se os segmentos podem formar um triângulo - a soma de dois lados deve ser menor que o terceiro - e imprime o resultado formatado com cores
if (lado1 < lado2+lado3) and (lado2 < lado3+lado1) and (lado3 < lado1+lado2):
    
    print("\n ==> Os segmentos \033[1;32mpodem formar\033[m um triângulo!")

else:

    print("\n ==> Os segmentos \033[1;31mnão são capazes de formar\033[m um triângulo")
