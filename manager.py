
tasks = []

def menu():
    print("\n menu do gerenciador de lista de tarefas:")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Atualizar tarefa")
    print("4 - tarefa concluida")
    print("5 - Deletar tarefa")
    print("6 - Sair\n")

def add_task(task):
    task = {"task": task, "completed": False}
    tasks.append(task)
    print(f"Tarefa {task['task']} adicionada com sucesso")
    return

def list_tasks():    
    if len(tasks) == 0:
        print("Nenhuma tarefa encontrada")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index} - {task['task']} - status: {'concluida' if task['completed'] else 'pendente'}")
    return

def update_task(new_task, indice):
    try:
        new_indice = int(indice)- 1
        if new_indice >= 0 and new_indice < len(tasks):
            tasks[new_indice]['task'] = new_task
            print("Tarefa atualizada com sucesso \n")
            return
        print("Tarefa não encontrada")
    except ValueError:
        print("Tarefa não encontrada") 

def change_status_done(indice):
    new_indice = int(indice) - 1
    if new_indice >= 0 and new_indice < len(tasks):
        tasks[new_indice]['completed'] = True
        print("Tarefa concluida \n")
        return
    print("Tarefa não encontrada")
    
def delete_task(indice):
    try:
        new_indice = int(indice) - 1
        if new_indice >= 0 and new_indice < len(tasks):
            tasks.pop(new_indice)
            print("Tarefa deletada com sucesso \n")
            return
        print("Tarefa não encontrada")
    except ValueError:
        print("\n Tarefa não encontrada")

menu()
optins = input("Digite a opção desejada: ")

while (optins != "6"):

    if optins == "1":
        task = input("Digite a tarefa: ")
        add_task(task)

    elif optins == "2":
        print("Tarefas: ")
        list_tasks()

    elif optins == "3":
        list_tasks()
        indice = input("Digite o indice da tarefa que deseja atualizar: ")
        new_task = input("Digite a nova tarefa: ")
        update_task(new_task, indice)
         
    elif optins == "4":
        list_tasks()
        indice = input("Digite o indice da tarefa que deseja concluir: ")
        change_status_done(indice)
        
    elif optins == "5":
        list_tasks()
        indice = input("Digite o indice da tarefa que deseja atualizar: ")
        delete_task(indice)
        
    elif optins == "6":
        print("Saindo do programa")
        break
    else:
        print("Opção inválida")

    menu()
    optins = input("Digite a opção desejada: ")
