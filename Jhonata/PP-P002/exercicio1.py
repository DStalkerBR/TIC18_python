def lista_tarefas (tarefas):
    print("\nTo Do List: ")
    for tarefa in tarefas:        
        print(f"{tarefa['id']}. {tarefa['descricao']} {tarefa['status']}")

def registrar_tarefa(tarefas, nova_tarefa):
    tarefa = {'id': str(len(tarefas) + 1), 'descricao': nova_tarefa, 'status': '[ ]'}
    tarefas.append(tarefa)
    print(f"Tarefa \"{tarefa['id']}. {tarefa['descricao']}\" registrada!!")

def realizar_tarefa (tarefas, identificador):
    for index, tarefa in enumerate(tarefas):
        if tarefa['id'] == identificador:
            tarefa['status'] = '[x]'
            tarefas.insert(0, tarefas.pop(index))
            print (f"Tarefa \"{tarefa['id']}. {tarefa['descricao']}\" realizada!!")
            break
    else:
        print(f"Tarefa com id {identificador} não encontrada!!")
        
def editar_tarefa (tarefas, identificador):
    for index, tarefa in enumerate(tarefas):
        if tarefa['id'] == identificador :
            print("Tarefa encontrada:")
            print(f"{tarefa['id']}. {tarefa['descricao']} {tarefa['status']}")
            nova_tarefa = input("Nova descrição da tarefa: ")
            tarefa['descricao'] = nova_tarefa
            print (f"Tarefa editada!!")
            

def main ():
    tarefas = [
        {'id': '1', 'descricao': 'Preparar a marmita', 'status': '[x]'},
        {'id': '2', 'descricao': 'Arrumar a mochila', 'status': '[ ]'},
        {'id': '3', 'descricao': 'Fechar as janelas', 'status': '[ ]'}
    ]

    # Adiciona uma nova tarefa
    nova_tarefa = input('Informe a descrição de uma nova tarefa: ').capitalize()
    registrar_tarefa(tarefas, nova_tarefa)
    
    # Realiza uma tarefa
    id_realizar_tarefa = input("Informe o identificador da tarefa para realizar: ")
    realizar_tarefa(tarefas, id_realizar_tarefa)
            
    # Edita uma tarefa
    id_editar_tarefa = input("Informe o identificador da tarefa para editar: ")
    editar_tarefa(tarefas, id_editar_tarefa)
    
    lista_tarefas(tarefas)


if __name__ == '__main__':
   main()