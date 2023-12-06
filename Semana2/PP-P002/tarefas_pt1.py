# Lista de tarefas
tarefas = []

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
        listar_tarefas()
    elif opcao == 2:
        registrar_tarefa()
    elif opcao == 3:
        marcar_tarefa_realizada()
    elif opcao == 4:
        editar_tarefa()
    elif opcao == 5:
        print("Saindo do aplicativo ToDoList. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
