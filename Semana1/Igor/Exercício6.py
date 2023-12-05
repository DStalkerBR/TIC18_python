L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(L[::-1])   # Reverso da lista
print(L[-1::])   # Último elemento da lista
print(L[:-1:])   # Lista sem o último elemento
print(L[::-2])   # Reverso da lista pulando de dois em dois
print(L[-2::])   # Últimos dois elementos da lista
print(L[:-2:])   # Lista sem os dois últimos elementos

# Resultados
print(L[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(L[-1::])   # [9]
print(L[:-1:])   # [1, 2, 3, 4, 5, 6, 7, 8]
print(L[::-2])   # [9, 7, 5, 3, 1]
print(L[-2::])   # [8, 9]
print(L[:-2:])   # [1, 2, 3, 4, 5, 6, 7]

ano_nascimento = int(input("Digite o ano de nascimento: "))
signos_chineses = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']

signo = signos_chineses[ano_nascimento % 12]
print(f"O signo do zodíaco chinês para o ano de {ano_nascimento} é: {signo}")