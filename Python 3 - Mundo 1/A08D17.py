# Desafio 017 - Calcular o comprimento da hipotenusa de um triângulo retângulo usando o módulo math

# Importa a função hypot do módulo math, responsável pelo cálculo da hipotenusa
from math import hypot

# Solicita os valores dos catetos do triângulo retângulo ao usuário
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# Retorna o valor da hipotenusa com o uso da função hypot
print(f"O valor da hipotenusa desse triângulo retângulo é igual a {hypot(cateto_oposto,cateto_adjacente):.2f}")
