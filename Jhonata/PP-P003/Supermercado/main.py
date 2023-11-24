def main():
    while(True):
        # limpar_tela()
        menu = "1. Inserir um produto\n" \
            "2. Excluir um produto\n" \
            "3. Listar todos os produtos\n" \
            "4. Consultar o preço de um produto\n" \
            "5. Sair\n"

        print(menu)
        escolha = int(input("Escolha uma opção: "))
        match escolha:
            case 1:
                print("Inserir um produto")
                # inserir_produto(produto)
            case 2:
                print("Excluir um produto")
                # excluir_produto(codigo)
            case 3:
                print("Listar todos os produtos")
                 # listar_produtos()
            case 4:
                print("Consultar o preço de um produto")
                # consultar_preco(codigo)
            case 5:
                print("Sair")
                break
            case _:
                print("Opção inválida")
                break


if __name__ == '__main__':
    main()
