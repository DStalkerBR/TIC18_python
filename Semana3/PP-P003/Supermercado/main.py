from produtos import Produto, lista_produtos

# Lista de produtos (inicialmente vazia)
produtos = []

def inserir_produto():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ").capitalize()
    preco = float(input("Digite o preço do produto: "))
    
    novo_produto = Produto(codigo, nome, preco)
    produtos.append(novo_produto)
    print("Produto inserido com sucesso!\n")

def excluir_produto():
    codigo = input("Digite o código do produto a ser excluído: ")
    produtos[:] = [produto for produto in produtos if produto.codigo != codigo]
    print("Produto excluído com sucesso!\n")

def consultar_preco():
    codigo = input("Digite o código do produto para consultar o preço: ")
    produto_encontrado = next((produto for produto in produtos if produto.codigo == codigo), None)
    if produto_encontrado:
        print(f"Preço do produto '{produto_encontrado.nome}': R${produto_encontrado.preco:.2f}\n")
    else:
        print("Produto não encontrado.\n")

def main():
    while True:
        print("Opções:")
        print("1. Inserir um novo produto")
        print("2. Excluir um produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar o preço de um produto")
        print("5. Sair")

        opcao = int(input("Escolha uma opção (1 a 5): "))

        if opcao == 1:
            inserir_produto()
        elif opcao == 2:
            excluir_produto()
        elif opcao == 3:
            lista_produtos(produtos)
        elif opcao == 4:
            consultar_preco()
        elif opcao == 5:
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
