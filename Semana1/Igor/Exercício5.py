print("Operadores Aritméticos : ")
a = 5.0
b = 2.0
resultado = a + b
print("soma : ",resultado)

resultado = a - b
print("Subtração :", resultado)

resultado = a * b
print("Multiplicação :", resultado)

resultado = a ** b
print("Potenciação :", resultado)

resultado = a / b
print("Divisão :", resultado) # Saída: 2.5 (divisão de ponto flutuante)


menor_potencia_de_2 = 2.0 ** -1022  # Utilizando o operador de exponenciação, mostra a maior e a menor potência de 2 representável
maior_potencia_de_2 = (2.0 ** 1023) * (1.0 - (2.0 ** -52))  # Precisão máxima para float64

print(f"\nMenor potência de 2 representável: {menor_potencia_de_2}")
print(f"Maior potência de 2 representável: {maior_potencia_de_2}")

original = 10.0 #variáveis numéricas imutáveis
modificado = original + 5.0
print(f"\nOriginal: {original}")
print(f"Modificado: {modificado}")


# Verifique quais métodos estão disponíveis para as variáveis de ponto flutuante
x = 3.14
print(f"\nMétodos disponíveis para variáveis de ponto flutuante: {dir(x)}")