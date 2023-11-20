# Inicializando a lista de tarefas
tarefas = []

# Função para listar as tarefas
def listar_tarefas():
    print("Lista de Tarefas:")
    for idx, tarefa in enumerate(tarefas, start=1):
        print(f"{idx}. {tarefa}")

# Função para registrar uma nova tarefa
def registrar_tarefa(descricao):
    if descricao[0].isupper():  # Verifica se a descrição começa com maiúscula
        tarefas.append(f"{len(tarefas)+1}. {descricao} [ ]")
        print("Tarefa registrada!!!")
    else:
        print("A descrição da tarefa deve começar com maiúscula.")

# Função para marcar uma tarefa como realizada
def marcar_tarefa_realizada(identificador):
    try:
        idx = int(identificador) - 1
        if 0 <= idx < len(tarefas):
            tarefa = tarefas.pop(idx)
            tarefas.insert(0, f"{tarefa[:-3]}[x]")
            print("Tarefa realizada!!!")
        else:
            print("Identificador inválido.")
    except ValueError:
        print("Por favor, insira um identificador válido.")

# Função para editar uma tarefa
def editar_tarefa(identificador, nova_descricao):
    try:
        idx = int(identificador) - 1
        if 0 <= idx < len(tarefas):
            antigo_id, antiga_descricao = tarefas[idx].split(".", 1)
            tarefas[idx] = f"{antigo_id}.{nova_descricao} [{tarefas[idx][-3]}]"
            print("Tarefa editada!!!")
        else:
            print("Identificador inválido.")
    except ValueError:
        print("Por favor, insira um identificador válido.")

# Loop principal
while True:
    print("\nMenu:")
    print("1. Listar Tarefas")
    print("2. Registrar Nova Tarefa")
    print("3. Marcar Tarefa como Realizada")
    print("4. Editar Tarefa")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        listar_tarefas()
    elif escolha == "2":
        descricao = input("Digite a descrição da nova tarefa: ")
        registrar_tarefa(descricao)
    elif escolha == "3":
        identificador = input("Digite o identificador da tarefa a ser marcada como realizada: ")
        marcar_tarefa_realizada(identificador)
    elif escolha == "4":
        identificador = input("Digite o identificador da tarefa a ser editada: ")
        nova_descricao = input("Digite a nova descrição da tarefa: ")
        editar_tarefa(identificador, nova_descricao)
    elif escolha == "5":
        print("Saindo do aplicativo ToDoList. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")