# Desafio 057 - Ler o sexo de uma pessoa mas só aceitas os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor válido

# Solicita a entrada do usuário
sexo = input("Digite o seu sexo - [M] ou [F]: ").upper().strip()

# Verifica se o valor foi uma entrada válida ou não, e pede a digitação novamente até ser válido
while sexo not in "MF":
    sexo = input("\033[31mOPÇÃO INVÁLIDA!\033[m\nPor favor, digite o seu sexo - \033[33mapenas [M] ou [F]:\033[m ").upper()

# Retorna uma mensagem com o valor escolhido
if (sexo == "M"):
    print("Você escolheu a opção \033[34m[M] - sexo masculino.\033[m")

else:
    print("Você escolheu a opção \033[35m[F] - sexo feminino.\033[m")
