nome = "Igor Alex"# variável 'nome' com meu nome

espaco_indice = nome.index(" ") # Pega a posição do espaço em branco e separada o nome.
primeiro_nome = nome[:espaco_indice]
sobrenome = nome[espaco_indice + 1:]


ordem_alfabetica = sorted([primeiro_nome, sobrenome])# Verifique qual das duas novas variáveis antecede a outra na ordem alfabética usando Sorted
if ordem_alfabetica[0] == primeiro_nome:
    print(f"{primeiro_nome} antecede {sobrenome} na ordem alfabética.")
else:
    print(f"{sobrenome} antecede {primeiro_nome} na ordem alfabética.")


print(f"Quantidade de caracteres em {primeiro_nome}: {len(primeiro_nome)}") # Verificando quantidade de letras em cada parte do nome
print(f"Quantidade de caracteres em {sobrenome}: {len(sobrenome)}")


if primeiro_nome.lower() == primeiro_nome.lower()[::-1]:# Verificando se o nome é um palíndromo
    print(f"{primeiro_nome} é um palíndromo.")
else:
    print(f"{primeiro_nome} não é um palíndromo.")