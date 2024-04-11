FILEPATH = 'todos.txt'


def get_todos():
    with open(FILEPATH, 'r') as file:
        todos = file.readlines()
    return todos


def update_todos(todo):
    with open(FILEPATH, 'w') as file:
        file.writelines(todo)
