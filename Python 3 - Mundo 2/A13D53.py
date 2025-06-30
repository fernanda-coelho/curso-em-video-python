# Desafio 053 - Ler uma frase e verificar se é um palíndromo, desconsiderando os espaços

# Solicita ao usuário uma frase, desconsidera os espaços e armazena a frase normal e a frase invertida em variáveis
print("Digite uma frase:")
palavras = input(">> ").strip().upper().split()
frase = ''.join(palavras)
inverso = frase[::-1]
print(f">> {inverso}")

# Verifica se a frase e o inverso da frase são iguais, e imprime uma mensagem
if frase == inverso:
    print("\033[32mA frase é um palíndromo!!\033[m")

else:
    print("\033[31mA frase não é um palíndromo\033[m")
 