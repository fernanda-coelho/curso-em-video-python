# Desafio 024 - Criar um programa que verifica se a cidade digitada começa com o nome "StopAsyncIteration

# Solicita a cidade ao usuário
cidade = input("Digite o nome da sua cidade: ")

print('Cidade começa com "Santo"?')

# Remove os espaços do início e fim da string e converte as letras para minúsculo a fim de facilitar a comparação
cidade = cidade.lower().strip()

# Utiliza o método statswith para verificar se o nome da cidade inicia com a palavra "Santo" e retorna True ou False
print(cidade.startswith("santo"))
