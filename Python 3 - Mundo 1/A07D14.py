## Desafio 014 - Criar um conversor de temperatura (°C para °F)

## Solicita a temperatura em °C ao usuário
temperatura_celsius = float(input("Digite a temperatura em °C: "))

## Converte °C em °F
temperatura_fahrenheit = (temperatura_celsius * 1.8) + 32

## Imprime o resultado da conversão
print(f"{temperatura_celsius:.1f} °C são {temperatura_fahrenheit:.1f} °F")
