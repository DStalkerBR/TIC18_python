from abc import ABC, abstractmethod
from typing import List

class Data:
    def __init__(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano

    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return self.__dia == outraData.__dia and \
               self.__mes == outraData.__mes and \
               self.__ano == outraData.__ano

    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False

    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False

class AnaliseDados(ABC):
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados
        self.__lista = []

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

    def adicionaDado(self, dado):
        if not isinstance(dado, self.__tipoDeDados):
            raise ValueError("Tipo de dado incorreto")
        self.__lista.append(dado)

    def ordenaLista(self):
        self.__lista.sort()

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(str)

    def entradaDeDados(self):
        n = int(input("Quantos nomes deseja adicionar? "))
        for _ in range(n):
            nome = input("Digite um nome: ")
            self.adicionaDado(nome)

    def mostraMediana(self):
        self.ordenaLista()
        tamanho = len(self._AnaliseDados__lista)
        if tamanho % 2 == 0:
            mediana = self._AnaliseDados__lista[tamanho // 2 - 1]
        else:
            mediana = self._AnaliseDados__lista[tamanho // 2]
        print(f"Mediana dos nomes: {mediana}")

    def mostraMenor(self):
        print(f"Menor nome: {min(self._AnaliseDados__lista)}")

    def mostraMaior(self):
        print(f"Maior nome: {max(self._AnaliseDados__lista)}")

    def listarEmOrdem(self):
        self.ordenaLista()
        print("Lista de nomes em ordem:")
        for nome in self._AnaliseDados__lista:
            print(nome)

class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(Data)

    def entradaDeDados(self):
        n = int(input("Quantas datas deseja adicionar? "))
        for _ in range(n):
            dia = int(input("Digite o dia: "))
            mes = int(input("Digite o mês: "))
            ano = int(input("Digite o ano entre 2000 e 2100: "))
            data = Data(dia, mes, ano)
            self.adicionaDado(data)

    def mostraMediana(self):
        self.ordenaLista()
        tamanho = len(self._AnaliseDados__lista)
        if tamanho % 2 == 0:
            mediana = self._AnaliseDados__lista[tamanho // 2 - 1]
        else:
            mediana = self._AnaliseDados__lista[tamanho // 2]
        print(f"Mediana das datas: {mediana}")

    def mostraMenor(self):
        print(f"Menor data: {min(self._AnaliseDados__lista)}")

    def mostraMaior(self):
        print(f"Maior data: {max(self._AnaliseDados__lista)}")

    def listarEmOrdem(self):
        self.ordenaLista()
        print("Lista de datas em ordem:")
        for data in self._AnaliseDados__lista:
            print(data)

def main():
    nomes = ListaNomes()
    datas = ListaDatas()

    listaListas = [nomes, datas]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        lista.listarEmOrdem()  # Adicionando a chamada para listar em ordem
        print("___________________")

    # Iterador zip
    nomes = ["Alice", "Bob", "Charlie"]
    salarios = [5000, 6000, 7000]

    # Percorra as listas de nomes e salários
    print("\nIterador zip:")
    for nome, salario in zip(nomes, salarios):
        print(f"{nome}: R${salario}")

    # Iterador map
    salarios_reajustados = list(map(lambda x: x * 1.1, salarios))
    print("\nIterador map - Salários reajustados em 10%:")
    print(salarios_reajustados)

    # Iterador filter
    from datetime import date

    # Crie uma lista de datas
    datas = [Data(30, 3, 2010), Data(12, 4, 2018), Data(24, 5, 2020)]

    # Modifique o dia para o primeiro dia do mês nas datas anteriores a 2019
    datas = [Data(1, 1, 2019) if data < Data(1, 1, 2019) else data for data in datas]

    print("\nIterador filter - Datas modificadas:")
    for data in datas:
        print(data)

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
