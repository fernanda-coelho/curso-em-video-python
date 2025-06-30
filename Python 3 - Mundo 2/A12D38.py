# Desafio 038 - Ler dois números inteiros e mostrar qual é maior, ou se os dois são iguais

# Solicita dois números ao usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Verifica qual número é maior ou se ambos são iguais, e imprime o resultado de forma destacada e colorida no terminal
if (numero1 > numero2):

    print(f">> O primeiro número é maior \033[1;34m({numero1} > {numero2})\033[m")

elif (numero2 > numero1):

    print(f">> O segundo número é maior \033[1;34m({numero2} > {numero1})\033[m")

else:

    print(">> Não existe valor maior, ambos são iguais.")
