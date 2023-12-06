class Empregado:
    def __init__(self, nome, sobrenome, ano_nascimento, rg, ano_admissao, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
        self.rg = rg
        self.ano_admissao = ano_admissao
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome} {self.sobrenome} | Ano de Nascimento: {self.ano_nascimento} | RG: {self.rg} | Ano de Admissão: {self.ano_admissao} | Salário: R${self.salario:.2f}"
