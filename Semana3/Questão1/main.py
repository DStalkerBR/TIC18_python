# main.py
from supermercado import Supermercado

def menu():
    print("1. Inserir novo produto")
    print("2. Excluir produto")
    print("3. Listar todos os produtos")
    print("4. Consultar preço")
    print("0. Sair")

if __name__ == "__main__":
    mercado = Supermercado()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = input("Digite o código do produto: ")
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            mercado.inserir_produto(codigo, nome, preco)
        elif opcao == "2":
            codigo = input("Digite o código do produto a ser removido: ")
            mercado.excluir_produto(codigo)
        elif opcao == "3":
            mercado.listar_produtos()
        elif opcao == "4":
            codigo = input("Digite o código do produto para consultar o preço: ")
            mercado.consultar_preco(codigo)
        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")