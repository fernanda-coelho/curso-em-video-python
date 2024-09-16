# Desafio 04 - Criar um programa que mostra o tipo primitivo e as informações sobre o que o usuário digitou

# Solicita a entrada do usuário e armazena na variável 'teclado'
teclado = input("Digite algo pelo teclado: ")

# Imprime o tipo primitivo da variável e outras informações
print(f"O tipo primitivo de {teclado} é {type(teclado)}")
print(f"É alfanumérico? {teclado.isalnum()}")
print(f"Tem somente espaços? {teclado.isspace()}")
print(f"É um número? {teclado.isnumeric()}")
print(f"É alfabético? {teclado.isalpha()}")
print(f"Está em maiúsculas? {teclado.isupper()}")
print(f"Está em minúsculas? {teclado.islower()}")
print(f"Está capitalizada? {teclado.istitle()}")