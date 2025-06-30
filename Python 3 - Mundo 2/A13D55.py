# Desafio 055 - Ler o peso de cinco pessoas e mostrar o maior e menor peso lidos

# Itera de 1 a 5 solicitando o peso dos usuários
for cont in range(1,6):
    peso_user = float(input(f"Pessoa {cont} - Digite o seu peso em kg: "))

    # Verifica se é o primeiro usuário, e em caso positivo define o seu peso como o maior e o menor
    if (cont == 1):

        maior_peso = peso_user
        usuario_maior = cont
        menor_peso = peso_user
        usuario_menor = cont

    # Se não for o primeiro usuário a digitar o peso, verifica se os novos pesos digitados são maiores ou menores que os do primeiro usuário
    else:
            
        if (peso_user > maior_peso):

                maior_peso = peso_user
                usuario_maior = cont

        if (peso_user < menor_peso):
                
                menor_peso = peso_user
                usuario_menor = cont
        
# Imprime os resultados
print(f"\033[33mMAIOR PESO\033[m - \033[36mUSUÁRIO {usuario_maior}\033[m - \033[35m{maior_peso}kg\033[m")
print(f"\033[33mMENOR PESO\033[m - \033[36mUSUÁRIO {usuario_menor}\033[m - \033[35m{menor_peso}kg\033[m")
