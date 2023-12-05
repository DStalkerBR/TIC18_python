
from abc import ABC, abstractmethod

class Data:
    
    def __init__(self, dia = 1, mes = 1, ano = 2000):
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
        return  self.__dia == outraData.__dia and \
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

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = [] 

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles.
        '''
        print("Digite a quantidade de nomes que deseja inserir na lista: ")
        numero = int(input())
        for i in range(numero):
            nome = input(f"Digite o {i+1} nome: ")
            self.__lista.append(nome)

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)
        meio = tamanho//2
        mediana = lista_ordenada[meio] if tamanho % 2 == 1 else lista_ordenada[meio-1]
        print("Mediana dos Nomes: ", mediana)
        

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        print("Menor Nome: ", min(self.__lista))
        

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        print("Maior Nome: ", max(self.__lista))

    def __str__(self):
        return str(self.__lista)
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []  
    
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        print("Digite a quantidade de datas que deseja inserir na lista: ")
        numero = int(input())
        for i in range(numero):
            data = input("Digite a data no formato dd/mm/aaaa: ")
            dia, mes, ano = data.split("/")
            data = Data(int(dia), int(mes), int(ano))
            self.__lista.append(data)
    
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)
        meio = tamanho//2
        mediana = lista_ordenada[meio] if tamanho % 2 == 1 else lista_ordenada[meio-1]
        print("Mediana das Datas: ", mediana)
         
     
    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        print("Menor Data: ", min(self.__lista))
    
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        print("Maior Data: ", max(self.__lista))
    
    def __str__(self):
        return str([str(data) for data in sorted(self.__lista)])
        

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []      

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        print("Digite a quantidade de salários que deseja inserir na lista: ")
        numero = int(input())
        for i in range(numero):
            print("Digite o salário: ")
            salario = float(input())
            self.__lista.append(salario)
        

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        # Se a lista tiver um número par de elementos
        # a mediana é a média dos dois elementos do meio
        # Se a lista tiver um número ímpar de elementos
        # a mediana é o elemento do meio
        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)
        meio = tamanho//2
        mediana = lista_ordenada[meio] if tamanho % 2 == 1 else (lista_ordenada[meio-1] + lista_ordenada[meio])/2
        print("Mediana dos Salários: ", mediana)
              

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        print("Menor Salário: ", min(self.__lista))

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        print("Maior Salário: ", max(self.__lista))
    
    def __str__(self):
        return str(self.__lista)

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []    
    
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        print("Digite a quantidade de idades que deseja inserir na lista: ")
        numero = int(input())
        for i in range(numero):
            print("Digite a idade: ")
            idade = int(input())
            self.__lista.append(idade)
    
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)
        meio = tamanho//2
        mediana = lista_ordenada[meio] if tamanho % 2 == 1 else (lista_ordenada[meio-1] + lista_ordenada[meio])/2
        print("Mediana das Idades: ", mediana)
    
    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        print("Menor Idade: ", min(self.__lista))
    
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        print("Maior Idade: ", max(self.__lista))

    def __str__(self):
        return str(self.__lista)

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
        print("___________________")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
