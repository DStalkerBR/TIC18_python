from Menu import Menu 
from Empregado import Empregados as emps

def main():
    menu = Menu()
    empregados = emps()
    
    while True:
        menu.limpar_tela()
        menu.mostrar_menu()
        try:
            opc = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida!!!")
            continue
        
        match opc:
            case 1:
                empregados.inserir_empregado()
            case 2:
                empregados.excluir_empregado()
            case 3:
                empregados.listar_empregados()
            case 4:
                empregados.consultar_empregado()
            case 5:
                empregados.reajusta_dez_porcento()
            case 6:
                empregados.ler_dados_arquivo('lista_empregados.txt')
            case 7:
                empregados.imprimir_dados('lista_empregados.txt')
            case 0:
                print("Sair")
                break
            case _:
                print("Opção Inválida!!!")


if __name__ == "__main__":
    main()


