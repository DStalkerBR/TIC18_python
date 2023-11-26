import os
import csv
from pathlib import Path

def limpar_tela():
    '''
    Limpa a tela do terminal
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    
def pressionar_enter(mensagem = "Pressione ENTER para continuar..."):
    '''
    Pausa a execução do programa até que o usuário pressione ENTER
    
    Parametros
    ----------
    mensagem: str
        Mensagem a ser exibida antes de pressionar ENTER
    '''
    input(mensagem)
    
def inserir_empregado(empregados:list[dict]):
    '''
    Insere um empregado na lista de empregados
    
    Parametros
    ----------
    empregados: list[dict]
        lista de empregados
    '''
    limpar_tela()
    print("+---------------+----------------------+-----------+")
    print("|                   Inserir empregado               |")    
    print("+---------------+----------------------+-----------+")

    rg = input("RG: ")
    nome = input("Nome: ").capitalize()
    sobrenome = input("Sobrenome: ").capitalize()
    nascimento = int(input("Ano de nascimento: "))
    admissao = int(input("Ano de admissão: "))
    salario = round(float(input("Salário: ")),2)   

    empregados.append({'rg': rg, 'nome': nome, 'sobrenome': sobrenome, 'nascimento': nascimento, 'admissao': admissao,  'salario': salario})
    print("Empregado inserido com sucesso!")
    pressionar_enter()
    
def excluir_empregado(empregados:list[dict]):
    '''
    Exclui um empregado da lista de empregados
    
    Parametros
    ----------
    empregados: list[dict]
        lista de empregados
    '''
    limpar_tela()
    print("+---------------+----------------------+-----------+")
    print("|                   Excluir empregado               |")
    print("+---------------+----------------------+-----------+")
    rg_excluir = input("Digite o RG do empregado que deseja excluir: ")
    for empregado in empregados:
        if empregado['rg'] == rg_excluir:
            empregados.remove(empregado)
            print(f"Empregado '{empregado['nome']}' excluido com sucesso!")
            break
    else:
        print("Empregado não encontrado!")
    pressionar_enter()
    
def listar_empregados(empregados:list[dict]):
    '''
    Lista os empregados
    
    Parametros
    ----------
    empregados: list[dict]
        lista de empregados
    '''
    inicio = 0
    while inicio < len(empregados):
        limpar_tela()
        print("+---------------+----------------------+-------------------+-----------------+--------------+")
        print("|                                       Listar empregados                                   |") 
        print("+---------------+----------------------+-------------------+-----------------+--------------+")
        print("| RG            | Nome                 | Ano de Nascimento | Ano de Admissão | Salário      |")
        print("+---------------+----------------------+-------------------+-----------------+--------------+")

        for empregado in empregados[inicio:inicio+11]:
            nome_completo = empregado['nome'] + ' ' + empregado['sobrenome']
            salario = f"R${empregado['salario']:.2f}"
            print(f"| {empregado['rg']:<13} | {nome_completo:<20} | {empregado['nascimento']:<17} | {empregado['admissao']:<15} | {salario:<12} |")

        print("+---------------+----------------------+-------------------+-----------------+--------------+")
        inicio += 11
        if inicio < len(empregados):
            pressionar_enter("Pressione ENTER para para ir para página...")
        else:
            pressionar_enter("Saindo... Pressione ENTER para continuar...")
            
def consultar_salario(empregados:list[dict]):
    '''
    Consulta o salário de um empregado
    
    Parametros
    ----------
    empregados: list[dict]
        lista de empregados
    '''
    limpar_tela()
    print("+---------------+----------------------+-----------+")
    print("|                   Consultar salário              |")    
    print("+---------------+----------------------+-----------+")
    rg_consultar = input("Digite o RG do empregado que deseja consultar o salário: ")
    for empregado in empregados:
        if empregado['rg'] == rg_consultar:
            print(f"O salário de {empregado['nome']} é R${empregado['salario']:.2f}")
            break
    else:
        print("Empregado não encontrado!")
    pressionar_enter()
    
def reajusta_dez_porcento(empregados:list[dict]):
    '''
    Reajusta o salário de todos os empregados em 10%
    
    Parametros
    ----------
    empregados: list[dict]
        lista de empregados
    '''
    for empregado in empregados:
        empregado['salario'] = round(empregado['salario']*1.1, 2)
    print("Salários reajustados com sucesso!")
    pressionar_enter()

def main():
    caminho:Path = Path(__file__).with_name('empregados.txt')
    empregados:list[dict] = []
    
    if caminho.exists():
        with caminho.open(encoding='utf-8') as arquivo_csv:
            empregados = list(csv.DictReader(arquivo_csv)) 
        for empregado in empregados:
            empregado['nascimento'] = int(empregado['nascimento'])
            empregado['admissao'] = int(empregado['admissao'])
            empregado['salario'] = round(float(empregado['salario']), 2)
    else:
        print("O arquivo 'empregados.txt' não existe. Criando arquivo novo...")
        with caminho.open('w', encoding='utf-8', newline='') as arquivo_csv:
            nome_colunas = ['rg', 'nome', 'sobrenome', 'nascimento', 'admissao', 'salario']
            escritor:csv.DictWriter = csv.DictWriter(arquivo_csv, fieldnames=nome_colunas)
            escritor.writeheader()
            print("Arquivo 'empregados.txt' criado.")
            pressionar_enter()

    while True:
        limpar_tela()
        print("+---------------+----------------------+-----------+")
        print("|                   Menu de opções                 |")
        print("+---------------+----------------------+-----------+")
        print("| 1 - Inserir empregado                            |")
        print("| 2 - Excluir empregado                            |")
        print("| 3 - Listar empregados                            |")
        print("| 4 - Consultar salário                            |")
        print("| 5 - Reajustar salários em 10%                    |")
        print("| 6 - Sair                                         |")
        print("+---------------+----------------------+-----------+")
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida")
            pressionar_enter()
            continue
        match opcao:
            case 1:
                inserir_empregado(empregados)
            case 2:
                excluir_empregado(empregados)
            case 3:
                listar_empregados(empregados)
            case 4:
                consultar_salario(empregados)
            case 5:
                reajusta_dez_porcento(empregados)
            case 6:
                with caminho.open(mode= 'w', encoding='utf-8' ,newline='') as arquivo_csv:
                    escritor:csv.DictWriter = csv.DictWriter(arquivo_csv, fieldnames=empregados[0].keys())
                    escritor.writeheader()
                    escritor.writerows(empregados)
                break
            case _:
                print("Opção inválida!")
                pressionar_enter()
    
if __name__ == '__main__':
    main()