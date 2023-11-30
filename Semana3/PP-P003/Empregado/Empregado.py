class Empregado:
    def __init__(self, nome, rg, ano_admissao, salario ) -> None:
        self.__nome = nome
        self.__rg = rg
        self.__ano_admissao = ano_admissao
        self.__salario = salario

        self.__dict_empregado = {'nome': self.__nome, 'rg': self.__rg, 'ano_admissao': self.__ano_admissao, 'salario': self.__salario}
    
    @property
    def dict_empregado(self):
        return self.__dict_empregado
    
class Empregados:
    def __init__(self) -> None:
        self.__lista_empregados = []
    
    def inserir_empregado(self):
        print("----------------------")
        print("   Inserir Empregado    ")
        print("----------------------")
        nome = input("Nome do empregado: ")
        rg = input("RG do empregado: ")
        ano_admissao = input("Ano de admissão do empregado: ")
        salario = float(input("Salário do empregado: "))
        empregado = Empregado(nome.capitalize(), rg, ano_admissao, salario)
        self.__lista_empregados.append(empregado)
        print("Empregado inserido com sucesso!")
        input("Pressione uma tecla para sair")
    
    def excluir_empregado(self):
        print("----------------------")
        print("   Excluir Empregado    ")
        print("----------------------")
        rg = input("Digite o RG do empregado a ser excluído: ")
        for index, emp in enumerate(self.__lista_empregados):
            if(emp.dict_empregado['rg'] == rg):
                self.__lista_empregados.pop(index)
                print(f"Empregado {emp.dict_empregado['nome']} excluído com sucesso!!!")
                input("Pressione uma tecla para sair")
                break
        else:
            print("Empregado não encontrado")
            input("Pressione uma tecla para sair")
        
    def listar_empregados(self):
        print("------------------------")
        print("    Lista de Empregados   ")
        print("------------------------")
        self.__lista_empregados.sort(key=lambda emp:emp.dict_empregado['nome'])
        for emp in self.__lista_empregados:
            print(f"Empregado: {emp.dict_empregado['nome']}\
                  \nRG: {emp.dict_empregado['rg']}\
                  \nAno de admissão: {emp.dict_empregado['ano_admissao']}\
                  \nSalário: {emp.dict_empregado['salario']:.2f}\n")
        input("Pressione uma tecla para sair")
    
    def consultar_empregado(self):
        print("------------------------")
        print("    Consultar Empregado   ")
        print("------------------------")
        rg = input("Digite o RG do empregado a ser consultado: ")
        for emp in self.__lista_empregados:
            if(emp.dict_empregado['rg'] == rg):
                print(f"Empregado: {emp.dict_empregado['nome']}\
                      \nRG: {emp.dict_empregado['rg']}\
                      \nAno de admissão: {emp.dict_empregado['ano_admissao']}\
                      \nSalário: {emp.dict_empregado['salario']:.2f}")
                break
        else:
            print("Empregado não encontrado")
        input("Pressione uma tecla para sair")
    
    def reajusta_dez_porcento(self):
        print("------------------------")
        print("    Reajuste 10%   ")
        print("------------------------")
        for emp in self.__lista_empregados:
            emp.dict_empregado['salario'] *= 1.1
            print(f"Empregado: {emp.dict_empregado['nome']}\
                      \nRG: {emp.dict_empregado['rg']}\
                      \nAno de admissão: {emp.dict_empregado['ano_admissao']}\
                      \nSalário: {emp.dict_empregado['salario']:.2f}")
        input("Pressione uma tecla para sair")

    def ler_dados_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(',')
                empregado = {
                    'nome': dados[0],
                    'sobrenome': dados[1],
                    'ano_nascimento': int(dados[2]),
                    'RG': dados[3],
                    'ano_admissao': int(dados[4]),
                    'salario': float(dados[5])
                }
                self.__lista_empregados.append(empregado)
        return self.__lista_empregados
    
    def imprimir_dados(lista_empregados):
        for empregado in lista_empregados:
            print(f"Nome: {empregado['nome']} {empregado['sobrenome']},\
                    Ano de Nascimento: {empregado['ano_nascimento']}, \
                    RG: {empregado['RG']}, Ano de Admissão: {empregado['ano_admissao']}, \
                    Salário: {empregado['salario']:.2f}")
