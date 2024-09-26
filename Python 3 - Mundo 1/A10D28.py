# Desafio 028 - Fazer um programa para que o usuário tente acertar qual foi o número inteiro escolhido pelo computador entre 0 a 5 e mostrar se o usuário venceu ou perdeu

# Importa o método randint do módulo random para selecionar um número aleatório
from random import randint

# Gera um número aleatório entre 0 e 5 e armazena em uma variável
numero_aleatorio = randint(0, 6)

print("=~"*30)
print("DESAFIO - Tente acertar o número escolhido pelo computador!")
print("=~"*30)

# Solicita um número inteiro ao usuário
numero_usuario = int(input("Digite um número inteiro entre 0 a 5: "))

# Verifica se o número digitado é o mesmo que o número aleatório e retorna uma mensagem
if numero_aleatorio == numero_usuario:
    print("VOCÊ VENCEU!!!!")

else:
    print(f"Poxa, não foi dessa vez! O número era o {numero_aleatorio} :(")
