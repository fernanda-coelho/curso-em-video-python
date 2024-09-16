# Desafio 018 - Informar o seno, cosseno e tangente de um ângulo

# Importa o módulo math
import math

# Solicita o ângulo, em graus, ao usuário
angulo_graus = float(input("Digite o ângulo:\n >> "))

# Converte o ângulo em radianos com a função radians e calcula o seno, cosseno e tangente com as funções sin, cos e tan
angulo_rad = math.radians(angulo_graus)
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

# Imprime o valor de seno, cosseno e tangente formatado em 2 casas decimais para o ângulo digitado
print(f"Seno de {angulo_graus}° = {seno:.2f}")
print(f"Cosseno de {angulo_graus}° = {cosseno:.2f}")
print(f"Tangente de {angulo_graus}° = {tangente:.2f}")
