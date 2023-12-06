from empregado import Empregado
from empresa import Reajusta_dez_porcento

# Lista de empregados (inicialmente vazia)
empregados = []

# Função para ler empregados de um arquivo
def ler_empregados():
    with open("empregados.txt", 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(',')
            empregado = Empregado(*dados)
            empregados.append(empregado)

# Função para exibir a lista de empregados
def exibir_empregados():
    for empregado in empregados:
        print(empregado)
    print("\n")

# Aplicativo para testar a função
def main():
    # Lê empregados do arquivo
    ler_empregados()

    while True:
        print("Opções:")
        print("1. Exibir Lista de Empregados")
        print("2. Reajustar Salários em 10%")
        print("3. Sair")

        opcao = int(input("Escolha uma opção (1 a 3): "))

        if opcao == 1:
            exibir_empregados()
        elif opcao == 2:
            Reajusta_dez_porcento(empregados)
            print("Salários reajustados em 10%!\n")
        elif opcao == 3:
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
