from empresa import Empresa

def menu():
    print("1. Carregar dados dos empregados")
    print("2. Reajustar salários em 10%")
    print("3. Listar empregados")
    print("0. Sair")

if __name__ == "__main__":
    empresa = Empresa()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
             #arquivo = "arquivo.txt"  # Nome do  arquivo estava dando problema pra achar o arquvio txt não sei o pq.
            arquivo = r"C:\Users\igora\OneDrive\Documentos\TIC18_python\Semana3\Questão2\arquivo.txt"  # Caminho absoluto do arquivo
            empresa.carregar_dados(arquivo)
            print("Dados carregados com sucesso!")
        elif opcao == "2":
            empresa.reajusta_dez_porcento()
            print("Salários reajustados em 10%.")
        elif opcao == "3":
            empresa.listar_empregados()
        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")