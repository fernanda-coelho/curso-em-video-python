# Desafio 043 - Calcular o IMC e mostrar o status: <18.5 abaixo do peso, entre 18.5 e 25 peso ideal, 25 até 30 sobrepeso, 30 até 40 obesidade e acima de 40 obesidade mórbida

# Solicita o peso e a altura do usuário
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcula o imc de acordo com os dados digitados pelo usuário
imc = (peso/(altura**2))

# Verifica o status do IMC e imprime uma mensagem
if (imc < 18.5):

    print(f">> Você está \033[1;31mabaixo do peso\033[m. Seu IMC: {imc:.2f}")


elif (imc < 25):

    print(f">> Você está no \033[1;32mpeso ideal\033[m. Seu IMC: {imc:.1f}")


elif (imc < 30):

    print(f">> Você está com \033[1;33msobrepeso\033[m. Seu IMC: {imc:.1f}")


elif (imc < 40):

    print(f">> Você está com \033[1;34mobesidade\033[m. Seu IMC: {imc:.1f}")


else:
    print(f">> Você está com \033[1;35mobesidade mórbida\033[m. Seu IMC: {imc:.1f}")
