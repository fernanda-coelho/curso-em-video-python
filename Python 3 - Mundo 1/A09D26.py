# Desafio 026 - Ler uma frase e mostrar quantas vezes aparece a letra 'a', e em que posição aparece a primeira e a última vez.

# Solicita uma frase ao usuário, converte todas as letras para minúsculo e remove os espaços antes e depois da string
frase = input("Digite uma frase:\n>> ").lower().strip()

# Verifica quantas vezes a letra "a" aparece com o método count e imprime o resultado
print(f"A letra 'a' aparece {frase.count("a")} vezes na frase '{frase}'")

# Verifica a posição da primeira ocorrência da letra "a" na frase com o método find e soma 1, já que a contagem se inicia no 0, e imprime o resultado
print(f"Posição da primeira ocorrência: {frase.find("a")+1}")

# Verifica a posição da última ocorrência da letra "a" na frase com o método rfind, soma 1 e imprime o resultado
print(f"Posição da última ocorrência: {frase.rfind("a")+1}")
