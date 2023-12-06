from abc import ABC, abstractmethod

class DataFruta:
    
    def __init__(self, dados):
        self.__dados = dados

    @property
    def dados(self):
        return self.__dados

    def mostraMediana(self):
        dados_ordenados = sorted(self.__dados)
        tamanho = len(dados_ordenados)

        if tamanho % 2 == 0:
            # Se o tamanho for par, média dos dois valores do meio
            mediana = (dados_ordenados[tamanho // 2 - 1] + dados_ordenados[tamanho // 2]) / 2
        else:
            # Se o tamanho for ímpar, valor do meio
            mediana = dados_ordenados[tamanho // 2]

        return mediana

    def listarEmOrdem(self):
        return sorted(self.__lista)

    def __str__(self):
        return f"{self.__class__.__name__}({self.__dados})"


class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

    @abstractmethod
    def listarEmOrdem(self):
        pass

    @abstractmethod
    def iterarElementos(self):
        pass

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        num_elementos = int(input("Quantos nomes você deseja inserir? "))
        for _ in range(num_elementos):
            nome = input("Digite um nome: ").capitalize()
            self.__lista.append(nome)

    def mostraMediana(self):
        # Mostrar o nome que está no meio da lista
        meio = len(self.__lista) // 2
        print(f"Mediana: {self.__lista[meio]}")

    def mostraMenor(self):
        menor_nome = min(self.__lista)
        print(f"Menor nome: {menor_nome}")

    def mostraMaior(self):
        maior_nome = max(self.__lista)
        print(f"Maior nome: {maior_nome}")
    
    def listarEmOrdem(self):
        return sorted(self.__lista)
    
    def iterarElementos(self):
        for nome in self.__lista:
            yield nome

    def __str__(self):
        return f"{self.__class__.__name__}({self.__lista})"


class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(DataFruta))
        self.__lista = []        
    
    def entradaDeDados(self):
        num_elementos = int(input("Quantas datas você deseja inserir? "))
        for _ in range(num_elementos):
            # Aqui você pode criar objetos DataFruta e adicioná-los à lista
            dados = [input("Dia: "), input("Mês: "), input("Ano: ")]
            data_fruta = DataFruta(dados)
            self.__lista.append(data_fruta)

    def mostraMediana(self):
        # Mostrar a mediana das datas
        valores = [data_fruta.mostraMediana() for data_fruta in self.__lista]
        mediana = sum(valores) / len(valores)
        print(f"Mediana das datas: {mediana}")

    def mostraMenor(self):
        # Mostrar a menor data
        menor_data = min(self.__lista, key=lambda x: x.mostraMediana())
        print(f"Menor data: {menor_data}")

    def mostraMaior(self):
        # Mostrar a maior data
        maior_data = max(self.__lista, key=lambda x: x.mostraMediana())
        print(f"Maior data: {maior_data}")
    
    def listarEmOrdem(self):
        return sorted(self.__lista)
    
    def iterarElementos(self):
        for data in self.__lista:
            yield data

    def __str__(self):
        return f"{self.__class__.__name__}({self.__lista})"


class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self):
        num_elementos = int(input("Quantos salários você deseja inserir? "))
        for _ in range(num_elementos):
            salario = float(input("Digite um salário: "))
            self.__lista.append(salario)

    def mostraMediana(self):
        # Mostrar a mediana dos salários
        mediana = sum(self.__lista) / len(self.__lista)
        print(f"Mediana dos salários: {mediana}")

    def mostraMenor(self):
        # Mostrar o menor salário
        menor_salario = min(self.__lista)
        print(f"Menor salário: {menor_salario}")

    def mostraMaior(self):
        # Mostrar o maior salário
        maior_salario = max(self.__lista)
        print(f"Maior salário: {maior_salario}")
    
    def listarEmOrdem(self):
        return sorted(self.__lista)
    
    def iterarElementos(self):
        for salario in self.__lista:
            yield salario

    def __str__(self):
        return f"{self.__class__.__name__}({self.__lista})"


class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        num_elementos = int(input("Quantas idades você deseja inserir? "))
        for _ in range(num_elementos):
            idade = int(input("Digite uma idade: "))
            self.__lista.append(idade)

    def mostraMediana(self):
        # Mostrar a mediana das idades
        valores_ordenados = sorted(self.__lista)
        tamanho = len(valores_ordenados)

        if tamanho % 2 == 0:
            # Se o tamanho for par, média dos dois valores do meio
            mediana = (valores_ordenados[tamanho // 2 - 1] + valores_ordenados[tamanho // 2]) / 2
        else:
            # Se o tamanho for ímpar, valor do meio
            mediana = valores_ordenados[tamanho // 2]

        print(f"Mediana das idades: {mediana}")

    def mostraMenor(self):
        # Mostrar a menor idade
        menor_idade = min(self.__lista)
        print(f"Menor idade: {menor_idade}")

    def mostraMaior(self):
        # Mostrar a maior idade
        maior_idade = max(self.__lista)
        print(f"Maior idade: {maior_idade}")
    
    def listarEmOrdem(self):
        return sorted(self.__lista)
    
    def iterarElementos(self):
        for idade in self.__lista:
            yield idade

    def __str__(self):
        return f"{self.__class__.__name__}({self.__lista})"


def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        print(f"Lista em Ordem: {lista.listarEmOrdem()}")
        
        # Demonstração do Iterador zip
        print("\nIterador zip:")
        for nome, salario in zip(lista.iterarElementos(), salarios.iterarElementos()):
            print(f"Nome: {nome}, Salário: {salario}")

        # Demonstração do Iterador map
        print("\nIterador map:")
        reajuste_salarios = list(map(lambda x: x * 1.1, salarios.iterarElementos()))
        print(f"Salários reajustados: {reajuste_salarios}")

        # Demonstração do Iterador filter
        print("\nIterador filter:")
        datas.lista = list(map(lambda x: DataFruta(1, x.mes, x.ano) if x.ano < 2019 else x, datas.lista))
        print(f"Datas modificadas: {datas.listarEmOrdem()}")

        print("___________________")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()