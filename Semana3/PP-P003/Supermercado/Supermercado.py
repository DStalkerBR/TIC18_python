class Produto:
    def __init__(self, codigo, nome, preco ) -> None:
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco 
    
    @property
    def codigo(self):
        return self.__codigo 

    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco

class Produtos:
    def __init__(self) -> None:
        self.__lista_produtos = []
    
    def inserir_produto(self):
        print("----------------------")
        print("   Inserir Produto    ")
        print("----------------------")
        cod = input("Código do produto: ")
        if (cod not in [prod.codigo for prod in self.__lista_produtos]) and (len(cod) == 13):
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            produto = Produto(cod, nome.capitalize(), preco)
            self.__lista_produtos.append(produto)
            print("Produto inserido com sucesso!")
        else:
            print("Código do produto inválido ou já existente")
        input("Pressione uma tecla para sair")


    def excluir_produto(self):
        print("----------------------")
        print("   Excluir Produto    ")
        print("----------------------")
        cod = input("Digite o código do produto a ser excluído: ")
        for index, prod in enumerate(self.__lista_produtos):
            if(prod.codigo == cod):
                self.__lista_produtos.pop(index)
                print(f"Produto {prod.nome} excluído com sucesso!!!")
                input("Pressione uma tecla para sair")
                break
        else:
            print("Produto não encontrado")
            input("Pressione uma tecla para sair")
    
    def listar_produtos(self):
        print("------------------------")
        print("    Lista de Produtos   ")
        print("------------------------")
        self.__lista_produtos.sort(key=lambda prod:prod.preco)
        for prod in self.__lista_produtos:
            print(f"Produto: {prod.nome}\
                   \nCódigo: {prod.codigo}\
                   \nPreço: {prod.preco:.2f}\
                   \n----------------------\n")
        input("Pressione uma tecla para sair")    
    
    def consultar_produto(self):
        print("------------------------")
        print("    Consultar Produto   ")
        print("------------------------")
        cod = input("Digite o código do produto para consulta: ")
        for prod in self.__lista_produtos:
            if(prod.codigo == cod):
                print(f"Preço do produto {prod.nome}: R${prod.preco:.2f}")
                input("Pressione uma tecla para sair")
                break
        else:
            print("Produto não encontrado")
            input("Pressione uma tecla para sair")
            