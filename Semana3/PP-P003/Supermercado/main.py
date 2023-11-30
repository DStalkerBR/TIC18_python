from Supermercado.Menu import Menu 
from Supermercado.Supermercado import Produtos as prods

def main():
    menu = Menu()
    produtos = prods()
    
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
                produtos.inserir_produto()
            case 2:
                produtos.excluir_produto()
            case 3:
                produtos.listar_produtos()
            case 4:
                produtos.consultar_produto()
            case 0:
                print("Sair")
                break
            case _:
                print("Opção Inválida!!!")


if __name__ == "__main__":
    main()


