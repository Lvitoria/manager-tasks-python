# Gerenciador de Lista de Tarefas

Este é um simples gerenciador de lista de tarefas em Python que permite adicionar, visualizar, atualizar, concluir e deletar tarefas. O programa apresenta um menu interativo para o usuário escolher a ação desejada.

## Funcionalidades

1. **Adicionar tarefa**: Permite adicionar uma nova tarefa à lista.
2. **Ver tarefas**: Exibe todas as tarefas da lista, indicando seu status (pendente ou concluída).
3. **Atualizar tarefa**: Permite atualizar o conteúdo de uma tarefa existente.
4. **Concluir tarefa**: Marca uma tarefa como concluída.
5. **Deletar tarefa**: Remove uma tarefa da lista.
6. **Sair**: Encerra o programa.

## Como Usar

1. **Clone o repositório** ou copie o código para um arquivo `.py` em seu computador.

2. **Execute o script**:

    ```sh
    python manager.py
    ```

3. **Interaja com o menu** digitando o número correspondente à ação desejada.

### Exemplo de Uso

Ao executar o script, você verá o menu:

Menu do Gerenciador de Lista de Tarefas:
1 - Adicionar tarefa
2 - Ver tarefas
3 - Atualizar tarefa
4 - Concluir tarefa
5 - Deletar tarefa
6 - Sair


Digite o número da opção desejada e siga as instruções fornecidas.

### Estrutura do Código

O código está dividido em várias funções para facilitar a manutenção e a legibilidade:

- `menu()`: Exibe o menu de opções.
- `add_task(task)`: Adiciona uma nova tarefa à lista.
- `list_tasks()`: Lista todas as tarefas com seu status.
- `update_task(new_task, indice)`: Atualiza o conteúdo de uma tarefa específica.
- `change_status_done(indice)`: Marca uma tarefa como concluída.
- `delete_task(indice)`: Deleta uma tarefa específica.

### Exemplo de Adição de Tarefa

Para adicionar uma tarefa, selecione a opção `1` no menu e digite a descrição da tarefa:

Digite a opção desejada: 1
Digite a tarefa: Estudar Python
Tarefa 'Estudar Python' adicionada com sucesso


### Exemplo de Visualização de Tarefas

Para visualizar as tarefas, selecione a opção `2`:

Digite a opção desejada: 2
Tarefas:
1 - Estudar Python - status: pendente


### Exemplo de Atualização de Tarefa

Para atualizar uma tarefa, selecione a opção `3`, informe o índice da tarefa a ser atualizada e a nova descrição:

Digite a opção desejada: 3
Tarefas:
1 - Estudar Python - status: pendente
Digite o índice da tarefa que deseja atualizar: 1
Digite a nova tarefa: Estudar Python Avançado
Tarefa atualizada com sucesso


### Exemplo de Conclusão de Tarefa

Para concluir uma tarefa, selecione a opção `4` e informe o índice da tarefa:

Digite a opção desejada: 4
Tarefas:
1 - Estudar Python Avançado - status: pendente
Digite o índice da tarefa que deseja concluir: 1
Tarefa concluída


### Exemplo de Deleção de Tarefa

Para deletar uma tarefa, selecione a opção `5` e informe o índice da tarefa:

Digite a opção desejada: 5
Tarefas:
1 - Estudar Python Avançado - status: concluída
Digite o índice da tarefa que deseja deletar: 1
Tarefa deletada com sucesso


### Saindo do Programa

Para sair do programa, selecione a opção `6`:

Digite a opção desejada: 6
Saindo do programa


## Requisitos

- Python 3.x

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.


Este é um projeto simples para ilustrar a criação de um gerenciador de tarefas em Python. Sinta-se à vontade para expandi-lo e adicionar novas funcionalidades!
