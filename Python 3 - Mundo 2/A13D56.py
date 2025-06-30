# Desafio 056 - Desenvolver um programa que lê o nome, idade e sexo de 4 pessoas, e mostrar a média de idade, nome do homem mais velho e quantidade de mulheres abaixo de 20 anos

media = 0
quantidade_mulheres = 0
mais_velho_idade = 0

# Itera de 1 a 4 para solicitar os dados dos usuários
for cont in range(1,5):
    nome = input(f"\033[33mPessoa {cont} \033[m - Digite seu nome: ")
    idade = int(input(f"Idade: "))
    sexo = input(f"Sexo (M ou F): ").upper()
    print("")

    # Armazena as idades para calcular a média
    media += idade

    # Verifica se o usuário é homem e se é o homem mais velho
    if (sexo == "M") and (idade > mais_velho_idade):
        mais_velho_idade = idade
        mais_velho_pessoa = nome

    # Verifica se o usuário é mulher e se possui menos que 20 anos
    elif (sexo == "F") and (idade < 20):
        quantidade_mulheres += 1  

# Calcula a média de todas as idades digitadas
media = (media/4)

# Imprime os resultados de média, homem mais velho e quantidade de mulheres < 20 anos
print(f"\033[36mMédia das idades - {media} anos")
print(f"Homem mais velho - {mais_velho_pessoa.title()}, {mais_velho_idade} anos")
print(f"Mulheres abaixo de 20 anos - {quantidade_mulheres} \033[m")
