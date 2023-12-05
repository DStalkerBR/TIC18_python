from abc import ABC, abstractmethod

class Data:
    
    def __init__(self, dia = 1, mes = 1, ano = 2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 1900 or ano > 2100:
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
        elementos_lista = int(input("Digite a quantidade de nomes que deseja inserir: "))
        for i in range(elementos_lista):
            self.__lista.append(input("Digite o nome: "))
        print('Nomes inseridos com sucesso!')
        
    def mostraMediana(self):
        self.__lista.sort()
        if len(self.__lista) % 2 == 0:
            print(f'Mediana : {self.__lista[len(self.__lista)//2]}')
        else:
            print(f'Mediana : {self.__lista[len(self.__lista)//2]}')

    def mostraMenor(self): 
        print(f'Menor : {self.__lista[0]}')
    
    def mostraMaior(self):
        print(f'Maior : {self.__lista[-1]}')

    def __str__(self):
        pass
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        quantidade = int(input("Digite a quantidade de datas que deseja inserir: "))
        for i in range(quantidade):
            dia = int(input("Digite o dia: "))
            mes = int(input("Digite o mês: "))
            ano = int(input("Digite o ano: "))
            self.__lista.append(Data(dia, mes, ano))
        print('Datas inseridas com sucesso!')    

    def mostraMediana(self):
        self.__lista.sort()
        if len(self.__lista) % 2 == 0:
            print(f'Mediana : {self.__lista[len(self.__lista)//2]}')
        else:
            print(f'Mediana : {self.__lista[len(self.__lista)//2]}')
     
    def mostraMenor(self):
        print(f'Menor : {self.__lista[0]}')
        
    def mostraMaior(self):
        print(f'Maior : {self.__lista[-1]}')
    
    def __str__(self):
        pass

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self):
        quantidade = int(input("Digite a quantidade de salários que deseja inserir: "))
        for i in range(quantidade):
            self.__lista.append(float(input("Digite o salário: ")))
        print('Salários inseridos com sucesso!')

    def mostraMediana(self):
        self.__lista.sort()
        if len(self.__lista) % 2 == 0:
            print(f'Mediana : {self.__lista[len(self.__lista)//2]}')
        else:
            print(f'Mediana : {self.__lista[len(self.__lista)//2]}')

    def mostraMenor(self):
        print(f'Menor : {self.__lista[0]}')
        
    def mostraMaior(self):
        print(f'Maior : {self.__lista[-1]}')
        
    def __str__(self):
        pass

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        quantidade = int(input("Digite a quantidade de idades que deseja inserir: "))
        for i in range(quantidade):
            self.__lista.append(int(input("Digite a idade: ")))
        print('Idades inseridas com sucesso!')
        
    def mostraMediana(self):
        self.__lista.sort()
        if len(self.__lista) % 2 == 0:
            print(f'Mediana : {self.__lista[len(self.__lista)//2]}')
        else:
            print(f'Mediana : {self.__lista[len(self.__lista)//2]}')
    
    def mostraMenor(self):
        print(f'Menor : {self.__lista[0]}')
        
    
    def mostraMaior(self):
        print(f'Maior : {self.__lista[-1]}')
        
    def __str__(self):
        pass

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
