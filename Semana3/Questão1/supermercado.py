class Supermercado:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, codigo, nome, preco):
        produto = {"codigo": codigo, "nome": nome, "preco": preco}
        self.produtos.append(produto)
        print(f"Produto {nome} inserido com sucesso!")

    def excluir_produto(self, codigo):
        for produto in self.produtos:
            if produto["codigo"] == codigo:
                self.produtos.remove(produto)
                print(f"Produto removido com sucesso!")
                return
        print("Produto não encontrado.")

    def listar_produtos(self):
        for produto in self.produtos:
            print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: {produto['preco']:.2f}")

    def consultar_preco(self, codigo):
        for produto in self.produtos:
            if produto["codigo"] == codigo:
                print(f"O preço de {produto['nome']} é {produto['preco']:.2f}")
                return
        print("Produto não encontrado.")