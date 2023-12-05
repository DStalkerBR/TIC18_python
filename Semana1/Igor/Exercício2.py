import math


print("Operadores Aritméticos : ")
a = 5
b = 3
resultado = a + b
print("soma : ",resultado)


resultado = a - b
print("Subtração :", resultado)

resultado = a * b
print("Multiplicação :", resultado)

resultado = a ** b
print("Potenciação :", resultado)

b = 2
resultado = a / b
print("Divisão :", resultado) # Saída: 2.5 (divisão de ponto flutuante)

resultado = a // b
print("Divisão Inteira :", resultado)  # Saída: 2 (parte inteira da divisão)

resultado = a % b
print("Resto da Divisão :", resultado)  

print("Representação de numeros inteiros significativamente grandes : ( fatorial de 30)")
fatorial_30 = math.factorial(30)
print(f"Fatorial de 30: {fatorial_30}")


print("Variáveis Numéricas Imutáveis")
a = 5
b = a
a = a + 2

print("Variável 'a':", a)  # Saída: 7
print("Variável 'b':", b)  # Saída: 5

print("Métodos Disponíveis para Variáveis Inteiras :")
x = 10
print(dir(x))