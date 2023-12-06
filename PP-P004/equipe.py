from abc import ABC, abstractmethod
from typing import List
from datetime import datetime

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

    def dummy(self):
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
        print("Lista de nomes em ordem alfabética:")
        for nome in sorted(self._AnaliseDados__lista):
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
        print("Lista de datas em ordem crescente:")
        for data in sorted(self._AnaliseDados__lista):
            print(data)

class ListaSalarios(AnaliseDados):  # Adicionada a classe ListaSalarios
    def __init__(self):
        super().__init__(float)

    def entradaDeDados(self):
        salario = float(input("Digite um salário: "))
        self.adicionaDado(salario)

    def mostraMediana(self):
        self.ordenaLista()
        tamanho = len(self._AnaliseDados__lista)
        if tamanho % 2 == 0:
            mediana = (self._AnaliseDados__lista[tamanho // 2 - 1] + self._AnaliseDados__lista[tamanho // 2]) / 2
        else:
            mediana = self._AnaliseDados__lista[tamanho // 2]
        print(f"Mediana dos salários: {mediana}")

    def mostraMenor(self):
        print(f"Menor salário: {min(self._AnaliseDados__lista)}")

    def mostraMaior(self):
        print(f"Maior salário: {max(self._AnaliseDados__lista)}")

    def listarEmOrdem(self):
        print("Lista de salários em ordem crescente:")
        for salario in sorted(self._AnaliseDados__lista):
            print(salario)

class ListaIdades(AnaliseDados):  # Adicionada a classe ListaIdades
    def __init__(self):
        super().__init__(int)

    def entradaDeDados(self):
        idade = int(input("Digite uma idade: "))
        self.adicionaDado(idade)

    def mostraMediana(self):
        self.ordenaLista()
        tamanho = len(self._AnaliseDados__lista)
        if tamanho % 2 == 0:
            mediana = (self._AnaliseDados__lista[tamanho // 2 - 1] + self._AnaliseDados__lista[tamanho // 2]) / 2
        else:
            mediana = self._AnaliseDados__lista[tamanho // 2]
        print(f"Mediana das idades: {mediana}")

    def mostraMenor(self):
        print(f"Menor idade: {min(self._AnaliseDados__lista)}")

    def mostraMaior(self):
        print(f"Maior idade: {max(self._AnaliseDados__lista)}")

    def listarEmOrdem(self):
        print("Lista de idades em ordem crescente:")
        for idade in sorted(self._AnaliseDados__lista):
            print(idade)

def incluir_nome(lista):
    nome = input("Digite um nome: ")
    lista.adicionaDado(nome)
    print("Nome incluído com sucesso!")

def incluir_salario(lista):
    salario = float(input("Digite um salário: "))
    lista.adicionaDado(salario)
    print("Salário incluído com sucesso!")

def incluir_data(lista):
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano entre 2000 e 2100: "))
    data = Data(dia, mes, ano)
    lista.adicionaDado(data)
    print("Data incluída com sucesso!")

def incluir_idade(lista):
    idade = int(input("Digite uma idade: "))
    lista.adicionaDado(idade)
    print("Idade incluída com sucesso!")

def percorrer_listas(listas):
    for lista in listas:
        print(f"Conteúdo da lista {type(lista).__name__}:")
        for item in lista._AnaliseDados__lista:
            print(f"{item:.2f}" if isinstance(item, float) else item)
        print("___________________")

def calcular_folha_salarios(lista_salarios):
    reajuste_percentual = 10
    for i in range(len(lista_salarios._AnaliseDados__lista)):
        salario_atual = lista_salarios._AnaliseDados__lista[i]
        salario_reajustado = salario_atual * (1 + reajuste_percentual / 100)
        lista_salarios._AnaliseDados__lista[i] = salario_reajustado
    print("Folha de salários recalculada com sucesso!")

def modificar_datas_antes_2019(lista_datas):
    for i in range(len(lista_datas._AnaliseDados__lista)):
        data_atual = lista_datas._AnaliseDados__lista[i]
        if data_atual.ano < 2019:
            nova_data = Data(1, 1, 2019)
            lista_datas._AnaliseDados__lista[i] = nova_data
    print("Datas modificadas com sucesso!")

def main():
    nomes = ListaNomes()
    salarios = ListaSalarios()
    datas = ListaDatas()
    idades = ListaIdades()

    listas = [nomes, salarios, datas, idades]

    while True:
        print("\nMenu de Opções:")
        print("1. Incluir um nome na lista de nomes")
        print("2. Incluir um salário na lista de salários")
        print("3. Incluir uma data na lista de datas")
        print("4. Incluir uma idade na lista de idades")
        print("5. Percorrer as listas de nomes, salários, datas e idades")
        print("6. Calcular o valor da folha com um reajuste de 10%")
        print("7. Modificar o dia das datas anteriores a 2019")
        print("8. Sair")

        opcao = input("Escolha uma opção (1-8): ")

        if opcao == '1':
            incluir_nome(nomes)
        elif opcao == '2':
            incluir_salario(salarios)
        elif opcao == '3':
            incluir_data(datas)
        elif opcao == '4':
            incluir_idade(idades)
        elif opcao == '5':
            percorrer_listas(listas)
        elif opcao == '6':
            calcular_folha_salarios(salarios)
        elif opcao == '7':
            modificar_datas_antes_2019(datas)
        elif opcao == '8':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
