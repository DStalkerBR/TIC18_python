print("Caracteres numéricos e seus códigos:") # Imprime os caracteres numéricos e seus códigos ASCII
for i in range(10):
    print(f"'{i}' - {ord(str(i))}")


print("\nCaracteres numéricos e seus códigos em octal e hexadecimal:") # Modifica o comportamento do print para imprimir como caractere e número em octal e hexadecimal
for i in range(10):
    print(f"'{i}' - {ord(str(i))} - Octal: {oct(ord(str(i)))} - Hexadecimal: {hex(ord(str(i)))}")


caractere = input("\nDigite um caractere: ") # Lê um caractere da entrada padrão e imprime suas informações
print(f"'{caractere}' - {ord(caractere)} - Octal: {oct(ord(caractere))} - Hexadecimal: {hex(ord(caractere))}")

caractere_especial1 = 'ç' # Demonstra o uso de caracteres especiais em Python
caractere_especial2 = 'ã'
print(f"\nExemplo de caracteres especiais: '{caractere_especial1}' - {ord(caractere_especial1)}")
print(f"'{caractere_especial2}' - {ord(caractere_especial2)}")