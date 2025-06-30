# Desafio 042 - Refazer o desafio 35 acrescentando o recurso de mostrar que tipo de triângulo será formado: equilátero, isósceles ou escaleno.

# Solicita o comprimento das retas ao usuário
lado1 = float(input("Digite o comprimento da primeira reta: "))
lado2 = float(input("Digite o comprimento da segunda reta: "))
lado3 = float(input("Digite o comprimento da terceira reta: "))

# Verifica se os segmentos podem formar um triângulo - a soma de dois lados deve ser menor que o terceiro - e imprime o resultado formatado com cores
if (lado1 < lado2+lado3) and (lado2 < lado3+lado1) and (lado3 < lado1+lado2):
    
    print("\n ==> Os segmentos \033[1;32mpodem formar\033[m um triângulo!")

    if (lado1 == lado2 == lado3):

        print("     Tipo formado: TRIÂNGULO EQUILÁTERO")


    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 ==3):

        print("     Tipo formado: TRIÂNGULO ISÓSCELES")


    else:

        print("     Tipo formado: TRIÂNGULO ESCALENO")


else:

    print("\n ==> Os segmentos \033[1;31mnão são capazes de formar\033[m um triângulo")
