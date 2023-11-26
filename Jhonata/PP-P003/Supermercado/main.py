def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
def pressionar_enter(mensagem = "Pressione ENTER para continuar..."):
    input(mensagem)
    
def inserir_produto(produtos:list[dict]):
    limpar_tela()
    print("+---------------+----------------------+-----------+")
    print("|                   Inserir produto                |")    
    print("+---------------+----------------------+-----------+")

    codigo = str(int(produtos[-1]['codigo']) + 1).zfill(13)
    nome = input("Nome: ").capitalize()
    preco = float(input("Preço: "))   

    produtos.append({'codigo': codigo, 'nome': nome, 'preco': preco})
    print("Produto inserido com sucesso!")
    pressionar_enter()
    
def excluir_produto(produtos:list[dict]):
    limpar_tela()
    print("+---------------+----------------------+-----------+")
    print("|                   Excluir produto                |")
    print("+---------------+----------------------+-----------+")
    cod_excluir = input("Digite o código do produto que deseja excluir: ")
    for produto in produtos:
        if produto['codigo'] == cod_excluir:
            produtos.remove(produto)
            print(f"Produto '{produto['nome']}' excluido com sucesso!")
            break
    else:
        print("Produto não encontrado!")
    pressionar_enter()

def listar_produtos(produtos:list[dict]):    
    inicio = 0
    produtos_preco = sorted(produtos, key=lambda produto: produto['preco'])
    while inicio < len(produtos):
        limpar_tela()
        print("+---------------+----------------------+-----------+")
        print("|                   Lista de produtos              |")    
        print("+---------------+----------------------+-----------+")
        print("| Código        | Nome                 | Preço     |")
        print("+---------------+----------------------+-----------+")

        for produto in produtos_preco[inicio:inicio+11]:
            preco = f"R${produto['preco']:.2f}"
            print(f"| {produto['codigo']:<14}| {produto['nome']:<21}| {preco:<10}|")

        print("+---------------+----------------------+-----------+")
        inicio += 11
        if inicio < len(produtos_preco):
            pressionar_enter("Pressione ENTER para para ir para página...")
        else:
            pressionar_enter("Saindo... Pressione ENTER para continuar...")

def consultar_preco(produtos:list[dict]):
    limpar_tela()
    print("+---------------+----------------------+-----------+")
    print("|                   Consultar preço                |")    
    print("+---------------+----------------------+-----------+")
    cod_consultar = input("Digite o código do produto que deseja consultar: ")
    for produto in produtos:
        if produto['codigo'] == cod_consultar:
            print(f"O preço do produto {produto['nome']} é R${produto['preco']:.2f}")
            break
    else:
        print("Produto não encontrado!")
    pressionar_enter()

def main():
    produtos:list[dict] = [{'codigo': '0000000000001', 'nome': 'Arroz', 'preco': 10.0}, \
                            {'codigo': '0000000000002', 'nome': 'Feijão', 'preco': 8.0}, \
                            {'codigo': '0000000000003', 'nome': 'Macarrão', 'preco': 5.0}, \
                            {'codigo': '0000000000004', 'nome': 'Carne', 'preco': 25.0}, \
                            {'codigo': '0000000000005', 'nome': 'Frango', 'preco': 15.0}, \
                            {'codigo': '0000000000006', 'nome': 'Peixe', 'preco': 10.0}, \
                            {'codigo': '0000000000007', 'nome': 'Ovo', 'preco': 5.0}, \
                            {'codigo': '0000000000008', 'nome': 'Leite', 'preco': 3.0}, \
                            {'codigo': '0000000000009', 'nome': 'Café', 'preco': 5.0}, \
                            {'codigo': '0000000000010', 'nome': 'Açucar', 'preco': 3.0}, \
                            {'codigo': '0000000000011', 'nome': 'Sal', 'preco': 2.0}, \
                            {'codigo': '0000000000012', 'nome': 'Pão', 'preco': 5.0}]
    while(True):
        limpar_tela()
        menu =  "Supermercado\n\n" \
            "1. Inserir um produto\n" \
            "2. Excluir um produto\n" \
            "3. Listar todos os produtos\n" \
            "4. Consultar o preço de um produto\n" \
            "5. Sair\n"

        print(menu)
        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida")
            pressionar_enter()
            continue
        match escolha:
            case 1:
                inserir_produto(produtos)
            case 2:
                excluir_produto(produtos)
            case 3:
                listar_produtos(produtos)
            case 4:
                consultar_preco(produtos)
            case 5:
                print("Sair")
                break
            case _:
                print("Opção inválida")
                pressionar_enter()


if __name__ == '__main__':
    main()
