from abc import ABC, abstractmethod
from typing import Type

class Data:
    def __init__(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 2000 or ano > 2100:
            raise ValueError("Data inválida")
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
        if not isinstance(outraData, Data):
            return False
        return self.__dia == outraData.__dia and \
               self.__mes == outraData.__mes and \
               self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if not isinstance(outraData, Data):
            return False
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
        if not isinstance(outraData, Data):
            return False
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
    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostrarMediana(self):
        pass
    
    @abstractmethod
    def mostrarMenor(self):
        pass

    @abstractmethod
    def mostrarMaior(self):
        pass

    @abstractmethod
    def listarEmOrdem(self):
        pass

    @abstractmethod
    def percorrerNomesESalarios(self):
        pass

    @abstractmethod
    def calcularCustoFolhaPagamento(self):
        pass

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(str)
        self.__nomes = []
        self.__salarios = []
        self.__datas = []
        self.__idades = []

    def entradaDeDados(self):
        nome = input("Digite um nome: ")
        salario = float(input("Digite o salário: "))
        data = Data(int(input("Digite o dia: ")), int(input("Digite o mês: ")), int(input("Digite o ano: ")))
        idade = int(input("Digite a idade: "))

        self.__nomes.append(nome)
        self.__salarios.append(salario * 1.1)  # Aplica o reajuste de 10%
        self.__datas.append(data)
        self.__idades.append(idade)

    def mostrarMediana(self):
        sorted_salarios = sorted(self.__salarios)
        n = len(sorted_salarios)
        if n % 2 == 0:
            middle1 = sorted_salarios[n//2 - 1]
            middle2 = sorted_salarios[n//2]
            median = (middle1 + middle2) / 2
        else:
            median = sorted_salarios[n//2]
        print("Mediana dos salários:", median)

    def mostrarMenor(self):
        print("Menor salário:", min(self.__salarios))

    def mostrarMaior(self):
        print("Maior salário:", max(self.__salarios))    

    def listarEmOrdem(self):
        nomes_ordenados = sorted(self.__nomes)
        salarios_ordenados = sorted(self.__salarios)
        datas_ordenadas = sorted(self.__datas, key=lambda x: (x.ano, x.mes, x.dia))
        idades_ordenadas = sorted(self.__idades)

        print("Nomes:", nomes_ordenados)
        print("Salários:", salarios_ordenados)
        print("Datas:", datas_ordenadas)
        print("Idades:", idades_ordenadas)

        print("Menor salário:", min(salarios_ordenados))
        print("Maior salário:", max(salarios_ordenados))
        
        n = len(salarios_ordenados)
        if n % 2 == 0:
            middle1 = salarios_ordenados[n//2 - 1]
            middle2 = salarios_ordenados[n//2]
            median = (middle1 + middle2) / 2
        else:
            median = salarios_ordenados[n//2]
        print("Mediana dos salários:", median)
        
        print("Menor idade:", min(idades_ordenadas))
        print("Maior idade:", max(idades_ordenadas))
        
        n_idades = len(idades_ordenadas)
        if n_idades % 2 == 0:
            middle1_idade = idades_ordenadas[n_idades//2 - 1]
            middle2_idade = idades_ordenadas[n_idades//2]
            median_idade = (middle1_idade + middle2_idade) / 2
        else:
            median_idade = idades_ordenadas[n_idades//2]
        print("Mediana das idades:", median_idade)

        print("Menor data:", datas_ordenadas[0])
        print("Maior data:", datas_ordenadas[-1])

        n_datas = len(datas_ordenadas)
        if n_datas % 2 == 0:
            middle1_data = datas_ordenadas[n_datas//2 - 1]
            middle2_data = datas_ordenadas[n_datas//2]
            median_data = (middle1_data + middle2_data) / 2
        else:
            median_data = datas_ordenadas[n_datas//2]
        print("Mediana das datas:", median_data)

    def percorrerNomesESalarios(self):
        for nome, salario, data, idade in zip(self.__nomes, self.__salarios, self.__datas, self.__idades):
            print(f"Nome: {nome}, Salário: R$ {salario}, Data: {data}, Idade: {idade}")

    def calcularCustoFolhaPagamento(self):
        custo_folha = sum(self.__salarios)
        print(f"Custo da folha de pagamento com reajuste de 10%: R$ {custo_folha}")

    def calcularTamanhoNomes(self):
        return [len(nome) for nome in self.__nomes]

    def calcularNomePeloTamanho(self):
        tamanho_nomes = self.calcularTamanhoNomes()
        nome_tamanho_dict = dict(zip(self.__nomes, tamanho_nomes))
        return nome_tamanho_dict

    def mostrarMenorNome(self):
        nome_tamanho_dict = self.calcularNomePeloTamanho()
        menor_nome = min(nome_tamanho_dict, key=nome_tamanho_dict.get)
        print("Menor nome:", menor_nome)

    def mostrarMaiorNome(self):
        nome_tamanho_dict = self.calcularNomePeloTamanho()
        maior_nome = max(nome_tamanho_dict, key=nome_tamanho_dict.get)
        print("Maior nome:", maior_nome)

    def mostrarMedianaNomes(self):
        tamanho_nomes = self.calcularTamanhoNomes()
        n = len(tamanho_nomes)
        if n % 2 == 0:
            middle1 = tamanho_nomes[n//2 - 1]
            middle2 = tamanho_nomes[n//2]
            median = (middle1 + middle2) / 2
        else:
            median = tamanho_nomes[n//2]
        
        primeiro_nome_mediana = next(nome for nome, tamanho in zip(self.__nomes, tamanho_nomes) if tamanho == median)

        print("Mediana dos tamanhos dos nomes:", median)
        print("Primeiro nome com tamanho da mediana:", primeiro_nome_mediana)

class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(Type[Data])  
        self.__lista = []        
    
    def entradaDeDados(self):
        dia = int(input("Dia: "))
        mes = int(input("Mês: "))
        ano = int(input("Ano: "))
        data = Data(dia, mes, ano)
        self.__lista.append(data)
    
    def listarEmOrdem(self):
        print(sorted(self.__lista, key=lambda x: (x.ano, x.mes, x.dia)))

    def percorrerNomesESalarios(self, salarios):
        for data, salario in zip(self.__lista, salarios):
            print(f"{data}: R$ {salario}")

    def calcularCustoFolhaPagamento(self):
        print(" ")

    def mostrarMediana(self):
        print(" ")

    def mostrarMenor(self):
        print(" ")

    def mostrarMaior(self):
        print(" ")

    def __str__(self):
        return str([str(data) for data in self.__lista])
    def listarEmOrdem(self):
        datas_ordenadas = sorted(self.__lista, key=lambda x: (x.ano, x.mes, x.dia))
        print("Datas:", datas_ordenadas)

        print("Menor data:", datas_ordenadas[0])
        print("Maior data:", datas_ordenadas[-1])

        n_datas = len(datas_ordenadas)
        if n_datas % 2 == 0:
            middle1_data = datas_ordenadas[n_datas//2 - 1]
            middle2_data = datas_ordenadas[n_datas//2]
            median_data = (middle1_data + middle2_data) / 2
        else:
            median_data = datas_ordenadas[n_datas//2]
        print("Mediana das datas:", median_data)

class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(float)
        self.__lista = []        

    def entradaDeDados(self):
        salario = float(input("Digite um salário: "))
        self.__lista.append(salario * 1.1)  # Aplica o reajuste de 10%

    def mostrarMediana(self):
        sorted_salarios = sorted(self.__lista)
        n = len(sorted_salarios)
        if n % 2 == 0:
            middle1 = sorted_salarios[n//2 - 1]
            middle2 = sorted_salarios[n//2]
            median = (middle1 + middle2) / 2
        else:
            median = sorted_salarios[n//2]
        print("Mediana dos salários:", median)

    def mostrarMenor(self):
        print("Menor salário:", min(self.__lista))

    def mostrarMaior(self):
        print("Maior salário:", max(self.__lista))    
    
    def listarEmOrdem(self):
        print(sorted(self.__lista))

    def percorrerNomesESalarios(self, nomes):
        for nome, salario in zip(nomes, self.__lista):
            print(f"{nome}: R$ {salario}")

    def calcularCustoFolhaPagamento(self):
        custo_folha = sum(self.__lista)
        print(f"Custo da folha de pagamento com reajuste de 10%: R$ {custo_folha}")

    def __str__(self):
        return str(self.__lista)

class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__(int)
        self.__lista = []        
    
    def entradaDeDados(self):
        idade = int(input("Digite uma idade: "))
        self.__lista.append(idade)

    def mostrarMediana(self):
        sorted_idades = sorted(self.__lista)
        n = len(sorted_idades)
        if n % 2 == 0:
            middle1 = sorted_idades[n//2 - 1]
            middle2 = sorted_idades[n//2]
            median = (middle1 + middle2) / 2
        else:
            median = sorted_idades[n//2]
        print("Mediana das idades:", median)

    def mostrarMenor(self):
        print("Menor idade:", min(self.__lista))

    def mostrarMaior(self):
        print("Maior idade:", max(self.__lista))

    def listarEmOrdem(self):
        print(sorted(self.__lista))

    def percorrerNomesESalarios(self, salarios):
        for idade, salario in zip(self.__lista, salarios):
            print(f"Idade: {idade}, Salário: R$ {salario}")

    def calcularCustoFolhaPagamento(self):
        
        print(" ")

    def __str__(self):
        return str(self.__lista)

def exibir_menu():
    print("Escolha uma opção:")
    print("1. Incluir um nome na lista de nomes")
    print("2. Incluir um salário na lista de salários")
    print("3. Incluir uma data na lista de datas")
    print("4. Incluir uma idade na lista de idades")
    print("5. Percorrer as listas de nomes e salários")
    print("6. Calcular o valor da folha com um reajuste de 10%")
    print("7. Modificar o dia das datas anteriores a 2019")
    print("8. Sair do programa")

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = {"1": nomes, "2": salarios, "3": datas, "4": idades}

    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")

        switch_dict = {
            "1": lambda: listaListas["1"].entradaDeDados(),
            "2": lambda: listaListas["2"].entradaDeDados(),
            "3": lambda: listaListas["3"].entradaDeDados(),
            "4": lambda: listaListas["4"].entradaDeDados(),
            "5": lambda: [lista.listarEmOrdem() for lista in listaListas.values()],
            "6": lambda: [lista.calcularCustoFolhaPagamento() for lista in listaListas.values() if isinstance(lista, ListaNomes) or isinstance(lista, ListaSalarios)],
            "7": lambda: datas.modificarDatasAnteriores2019(),
            "8": lambda: print("Saindo do programa...")
        }

        switch_dict.get(opcao, lambda: print("Opção inválida. Digite um número de 1 a 8."))()

        if opcao == "8":
            break

if __name__ == "__main__":
    main()

