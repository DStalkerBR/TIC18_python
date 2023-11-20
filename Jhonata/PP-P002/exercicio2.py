import csv
from pathlib import Path
from os import system

def lista_tarefas (tarefas):
    """
    Imprime uma lista de tarefas com base nas tarefas fornecidas.

    Parameters:
        tarefas (list): Uma lista de dicionários que representam as tarefas. Cada dicionário contém as seguintes chaves:
            - id (int): O ID da tarefa.
            - descricao (str): A descrição da tarefa.
            - status (str): O status da tarefa.

    Returns:
        None
    """
    print("\nTo Do List: ")
    for tarefa in tarefas:        
        print(f"{tarefa['id']}. {tarefa['descricao']} {tarefa['status']}")

def registrar_tarefa(tarefas, nova_tarefa):
    """
    Adiciona uma nova tarefa à lista de tarefas.

    Parameters:
        tarefas (list): A lista de tarefas.
        nova_tarefa (str): A descrição da nova tarefa.

    Returns:
        None
    """
    tarefa = {'id': str(len(tarefas) + 1), 'descricao': nova_tarefa, 'status': '[ ]'}
    tarefas.append(tarefa)
    print(f"Tarefa \"{tarefa['id']}. {tarefa['descricao']}\" registrada!!")

def realizar_tarefa (tarefas, identificador):
    """
    Marca uma tarefa como concluída e a move para o topo da lista de tarefas.

    Parameters:
        tarefas (list): A lista de tarefas.
        identificador (str): O identificador da tarefa a ser concluída.

    Returns:
        None
    """
    for index, tarefa in enumerate(tarefas):
        if tarefa['id'] == identificador and tarefa['status'] == '[ ]':
            tarefa['status'] = '[x]'
            tarefas.insert(0, tarefas.pop(index))
            print (f"Tarefa \"{tarefa['id']}. {tarefa['descricao']}\" realizada!!")
            break
    else:
        print(f"Tarefa com id {identificador} já realizada ou não encontrada!!")
        
def editar_tarefa (tarefas, identificador):
    """
    Edita uma tarefa na lista de tarefas fornecida com base no identificador especificado.
    
    Parameters:
        - tarefas (list): Uma lista de dicionários que representam as tarefas.
        - identificador (int): O identificador da tarefa a ser editada.
        
    Returns:
        None
    """
    for tarefa in tarefas:
        if tarefa['id'] == identificador :
            print("Tarefa encontrada:")
            print(f"{tarefa['id']}. {tarefa['descricao']} {tarefa['status']}")
            nova_tarefa = input("Nova descrição da tarefa: ")
            tarefa['descricao'] = nova_tarefa
            print (f"Tarefa editada!!")
            break
    else:
        print(f"Tarefa com id {identificador} não encontrada!!")
            
def main ():
    """
    Executa a lógica principal do programa.
    
    Esta função realiza as seguintes ações:
    1. Lê as tarefas existentes de um arquivo CSV.
    2. Solicita ao usuário uma nova descrição de tarefa e a adiciona à lista de tarefas.
    3. Solicita ao usuário o ID de uma tarefa para marcar como concluída.
    4. Solicita ao usuário o ID de uma tarefa para editar e atualiza sua descrição.
    5. Atualiza o arquivo CSV com a lista de tarefas modificada.
    """
    tarefas = []
    
    # Define o caminho para o arquivo 'tarefas.txt' ao mesmo diretório desse programa. 
    # Este caminho será utilizado para realizar a leitura e escrita das tarefas no arquivo.
    p = Path(__file__).with_name('tarefas.txt')
      
    # Abre arquivo, carrega as tarefas e modifica as tarefas existentes
    if p.exists():
        with p.open() as arquivo_csv:
            tarefas = list(csv.DictReader(arquivo_csv)) 
    else:
        print("O arquivo 'tarefas.txt' não existe. Criando arquivo novo...")
        with p.open('w', newline='') as arquivo_csv:
            writer = csv.DictWriter(arquivo_csv, fieldnames=['id', 'descricao', 'status'])
            writer.writeheader()
            print("Arquivo 'tarefas.txt' criado.")
            input("Pressione qualquer tecla para continuar...")
        
    while True:
        system("cls||clear")
        
        # Lista as tarefas
        lista_tarefas(tarefas)  
        
        print("\n\nMenu:")
        print("1. Adicionar uma nova tarefa")
        print("2. Realizar uma tarefa")
        print("3. Editar uma tarefa")
        print("0. Sair do programa")
        
        escolha = input("Escolha uma opção: ")
        
        match escolha:
            case "1":
                # Adiciona uma nova tarefa
                nova_tarefa = input("Informe a descrição de uma nova tarefa: ").capitalize()
                registrar_tarefa(tarefas, nova_tarefa)
            case "2":
                # Realiza uma tarefa
                id_realizar_tarefa = input("Informe o identificador da tarefa para realizar: ")
                realizar_tarefa(tarefas, id_realizar_tarefa)
            case "3":
                # Edita uma tarefa
                id_editar_tarefa = input("Informe o identificador da tarefa para editar: ")
                editar_tarefa(tarefas, id_editar_tarefa)              
            case "0":
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")
                
        input("Pressione qualquer tecla para continuar...")
        
    # Atualizar arquivo
    with p.open('w', newline='') as arquivo:
        print("Atualizando o arquivo com as tarefas...")
        lista_tarefas(tarefas)
        header = tarefas[0].keys()  
        writer = csv.DictWriter(arquivo, fieldnames=header)
        writer.writeheader()  
        writer.writerows(tarefas)  

if __name__ == '__main__':
   main()