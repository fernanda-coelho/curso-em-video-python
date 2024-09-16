# Desafio 016 - Mostrar a porção inteira de um número digitado

# Importa o módulo math para utilizar a função trunc, que retorna a parte inteira de um número
from math import trunc

# Solicita um número float ao usuário
numero = float(input("Digite um número real: "))

# Imprime a parte inteira do valor digitado, descartando a parte decimal
print(f"A parte inteira do número {numero} corresponde a {trunc(numero)}")