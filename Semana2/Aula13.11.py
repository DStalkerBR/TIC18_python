lista = [1,2,3,4,5,6,7,8,9]

print("Lista original = ",lista)

lista.append(10)

print(f"Usando o append: Lista = {lista}")

lista.insert(4,4.5)
print(f"Usando o insert na posição 4: Lista = {lista}")

lista.pop(4)
print(f"Usando o pop na posição 4: Lista = {lista}")

lista.reverse()
print(f"Usando o reverse na lista: Lista = {lista}")
lista.reverse()

#[inicio:fim:incremento]
print(f"Printando lista a partir da posição 5: Lista = {lista[5::]}")
print(f"Printando lista sem os 3 ultimos elementos: Lista = {lista[:-3:]}")
print(f"Printando lista de 2 em 2 elementos: Lista = {lista[::2]}")
print(f"Printando lista por posição par: Lista = {lista[1::2]}")

#Tuplas
a,b,c = 1, 'A', "Tupla"
print(f"Printando a tupla a,b,c: {(a,b,c)}")
a,b = "troca a", "troca b"
a,b = b,a
print(f"Fazendo a troca da tupla a,b por b,a:\nValor de a = {a}\nValor de b = {b}")

#Dicionários
meuReg = {'Nome':'David','Idade': 22,'Altura': 1.78}

print("Dicionário:")

for item in meuReg:
    print(f"Atributo: {item} | Valor: {meuReg[item]}")

#Conjuntos
p = {1,2,3,4,5}
i = {1,3,5}

print(f"Intersecção = {p.intersection(i)}")