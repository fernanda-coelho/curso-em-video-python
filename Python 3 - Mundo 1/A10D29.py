# Desafio 029 - Escrever um programa que lê a velocidade de um carro em km/h, e que se ultrapassar 80km/h mostrar uma mensagem de que ele será multado. A multa custa R$7,00 a cada km acima do limite.

# Solicita a velocidade do carro ao usuário
velocidade = float(input("Digite a velocidade que o carro estava, em km/h \n>> "))

# Verifica se a velocidade estava acima do limite de 80
if (velocidade > 80):
    
    valor_multa = (velocidade - 80) * 7 # Calcula o valor da multa

    print(f"Você será multado em R${valor_multa:.2f} por estar acima de 80km/h") # Imprime o valor e formata para 2 casas decimais

else:
    print("Parabéns! Você estava dentro dos limites de velocidade.") 
