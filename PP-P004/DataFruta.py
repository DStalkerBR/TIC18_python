
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
    
    @abstractmethod
    def listarEmOrdem(self):
        pass

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = [] 
        # self.__lista.extend(["João", "Maria", "José", "Ana", "Pedro", "Paulo", "Carlos", "Márcia"])

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
        

    def listarEmOrdem(self):
        '''
        Este método ordena a lista e mostra os elementos
        '''
        lista_ordenada = sorted(self.__lista)
        print("Lista de Nomes: ", lista_ordenada)
        
    @property
    def lista(self):
        return self.__lista
    
    @lista.setter
    def lista(self):
        raise ValueError("Não é possível alterar a lista de nomes")

    def __str__(self):
        return str(self.__lista)
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []  
        # self.__lista.extend([ Data(15, 7, 2020),Data(3, 11, 2008),Data(22, 5, 2001),Data(8, 2, 2003),Data(12, 9, 2005),Data(1, 12, 2004)])
    
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
        
    def listarEmOrdem(self):
        '''
        Este método ordena a lista e mostra os elementos
        '''
        lista_ordenada = sorted(self.__lista)
        print("Lista de Datas: ", [str(data) for data in lista_ordenada])
        
    @property
    def lista(self):
        return self.__lista
    
    @lista.setter
    def lista(self, lista):
        self.__lista = lista
    
    def __str__(self):
        return str([str(data) for data in sorted(self.__lista)])
        

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []   
        # self.__lista.extend([1500.50, 2300.75, 1800.25, 2500.0, 2000.99, 3000.45])


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
        
    def listarEmOrdem(self):
        '''
        Este método ordena a lista e mostra os elementos
        '''
        lista_ordenada = sorted(self.__lista)
        print("Lista de Salários: ", lista_ordenada)
        
    @property
    def lista(self):
        return self.__lista
    
    @lista.setter
    def lista(self, lista):
        raise ValueError("Não é possível alterar a lista de salários")
    
    def __str__(self):
        return str(self.__lista)

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []    
        #  self.__lista.extend([25, 30, 22, 35, 28, 40])

    
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
        
    def listarEmOrdem(self):
        '''
        Este método ordena a lista e mostra os elementos
        '''
        lista_ordenada = sorted(self.__lista)
        print("Lista de Idades: ", lista_ordenada)
        
    @property
    def lista(self):
        return self.__lista
    
    @lista.setter
    def lista(self, lista):
        raise ValueError("Não é possível alterar a lista de idades")

    def __str__(self):
        return str(self.__lista)


class Estatisticas:
    def __init__(self, listaListas):
        self.__lista = listaListas
    
    def nomeSalarios(self):        
        print("Nome\t\tSalário")
        print("-" * 25)
        for nome, salario in zip(self.__lista[0].lista, self.__lista[2].lista):
            print("{:<10}\t{:.2f}".format(nome, salario))
    
    def reajusteSalarios(self):
        print("Custo da folha de pagamento:")
        print(sum(self.__lista[2].lista))
        print("Custo da folha de pagamento se os salários fossem reajustados em 10%:")
        print(sum(map(lambda x: x*1.1, self.__lista[2].lista)))
            
    def modificaDatas(self):
        datas_anteriores_2019 = filter(lambda x: x.ano < 2019, self.__lista[1].lista)
        datas_modificadas = map(lambda x: Data(1, x.mes, x.ano), datas_anteriores_2019)
        datas_posteriores_2019 = filter(lambda x: x.ano >= 2019, self.__lista[1].lista)
        
        self.__lista[1].lista = list(datas_modificadas) + list(datas_posteriores_2019)
        print ("Datas anteriores a 2019 modificadas:")
        for data in self.__lista[1].lista:
            print(data)
            
def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()
    
    listaListas = [nomes, datas, salarios, idades]
    
    estatisticas = Estatisticas(listaListas)
    
    for lista in listaListas:
        lista.entradaDeDados()
        lista.listarEmOrdem()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        lista.listarEmOrdem()
        
        print("___________________")
        
    
    print("Estatisticas:")
    estatisticas.nomeSalarios()
    print("___________________")
    estatisticas.reajusteSalarios()
    print("___________________")
    estatisticas.modificaDatas()
    print("___________________")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
