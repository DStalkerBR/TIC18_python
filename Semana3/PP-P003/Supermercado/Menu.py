import os

class Menu:
    def mostrar_menu(self):
        print("\tSuperMercado\
             \n-----------------------------\
             \n1 - Inserir novo produto\
             \n2 - Excluir produto cadastrado\
             \n3 - Listar produtos\
             \n4 - Consultar preço por código\
             \n0 - Sair")
    
    def limpar_tela(self):
         os.system('cls' if os.name == 'nt' else 'clear')