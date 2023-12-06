import os

# Caminho do arquivo
caminho_arquivo = "tarefas.txt"

def listar_tarefas():
    print("Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa['descricao']} {tarefa['status']}")

def registrar_tarefa():
    descricao = input("Digite a descrição da nova tarefa: ").capitalize()
    nova_tarefa = {'descricao': descricao, 'status': '[ ]'}
    tarefas.append(nova_tarefa)
    print("Tarefa registrada!!!")

def marcar_tarefa_realizada():
    listar_tarefas()
    identificador = int(input("Digite o identificador da tarefa a ser marcada como realizada: "))
    
    if 1 <= identificador <= len(tarefas):
        tarefa = tarefas.pop(identificador - 1)
        tarefa['status'] = '[x]'
        tarefas.insert(0, tarefa)
        print("Tarefa marcada como realizada!!!")
    else:
        print("Identificador inválido. Nenhuma alteração realizada.")

def editar_tarefa():
    listar_tarefas()
    identificador = int(input("Digite o identificador da tarefa a ser editada: "))
    
    if 1 <= identificador <= len(tarefas):
        nova_descricao = input("Digite a nova descrição da tarefa: ").capitalize()
        tarefas[identificador - 1]['descricao'] = nova_descricao
        print("Tarefa editada com sucesso!!!")
    else:
        print("Identificador inválido. Nenhuma alteração realizada.")

# Função para ler as tarefas do arquivo
def ler_tarefas():
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            return [linha.strip() for linha in linhas]
    else:
        return []

# Função para escrever as tarefas no arquivo
def escrever_tarefas():
    with open(caminho_arquivo, 'w') as arquivo:
        for tarefa in tarefas:
            arquivo.write(f"{tarefa['descricao']} {tarefa['status']}\n")

# Lista de tarefas
tarefas = [{'descricao': 'Preparar a marmita', 'status': '[x]'}, {'descricao': 'Arrumar a mochila', 'status': '[ ]'}]

# Exemplo de utilização
while True:
    print("\nOpções:")
    print("1. Listar Tarefas")
    print("2. Registrar Nova Tarefa")
    print("3. Marcar Tarefa como Realizada")
    print("4. Editar Tarefa")
    print("5. Sair")

    opcao = int(input("Escolha uma opção (1 a 5): "))

    if opcao == 1:
        # Listar tarefas lendo do arquivo
        tarefas = [{'descricao': linha.split()[1], 'status': linha.split()[2]} for linha in ler_tarefas()]
        listar_tarefas()
    elif opcao == 2:
        registrar_tarefa()
        # Escrever as tarefas no arquivo após registrar uma nova tarefa
        escrever_tarefas()
    elif opcao == 3:
        marcar_tarefa_realizada()
        # Escrever as tarefas no arquivo após marcar uma tarefa como realizada
        escrever_tarefas()
    elif opcao == 4:
        editar_tarefa()
        # Escrever as tarefas no arquivo após editar uma tarefa
        escrever_tarefas()
    elif opcao == 5:
        print("Saindo do aplicativo ToDoList. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
