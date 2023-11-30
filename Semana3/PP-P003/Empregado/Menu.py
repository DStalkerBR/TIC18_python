import os

class Menu:
    def mostrar_menu(self):
        print("\tEmpregados\
             \n-----------------------------\
             \n1 - Inserir novo empregado\
             \n2 - Excluir empregado cadastrado\
             \n3 - Listar empregados\
             \n4 - Consultar empregado por RG\
             \n5 - Reajustar 10% do salário\
             \n6 - Ler dados do arquivo \
             \n7 - Imprimir dados do arquivo \
             \n0 - Sair")
    
    def limpar_tela(self):
         os.system('cls' if os.name == 'nt' else 'clear')