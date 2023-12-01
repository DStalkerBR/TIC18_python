from datetime import datetime

class Empresa:
    def __init__(self):
        self.empregados = []

    def carregar_dados(self, arquivo):
        with open(arquivo, 'r') as file:
            for line in file:
                nome, sobrenome, nascimento, rg, admissao, salario = line.strip().split(',')
                # Convertendo a data de nascimento para o ano
                ano_nascimento = datetime.strptime(nascimento, '%Y-%m-%d').year
                empregado = {
                    "nome": nome,
                    "sobrenome": sobrenome,
                    "nascimento": ano_nascimento,
                    "rg": rg,
                    "admissao": int(admissao),
                    "salario": float(salario)
                }
                self.empregados.append(empregado)

    def reajusta_dez_porcento(self):
        for empregado in self.empregados:
            empregado["salario"] *= 1.1  # Aumento de 10%

    def listar_empregados(self):
        for empregado in self.empregados:
            print(f"Nome: {empregado['nome']} {empregado['sobrenome']}, Salário: R${empregado['salario']:.2f}")