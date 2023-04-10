FILEPATH = 'lista_activitati/store.txt'

def get_todos(cale_fisier=FILEPATH):
    with open(cale_fisier, "r") as file_local:
            todos_local = file_local.readlines()
    return todos_local        

def write_todos(todos_arg, cale_fisier=FILEPATH):
    with open(cale_fisier, "w") as file:
            file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello!")