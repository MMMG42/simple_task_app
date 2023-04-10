import functions
import time

data_cur = time.strftime('%b %d, %Y %H:%M:%S')
print('It is', data_cur)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos,"store.txt")
        
        
    elif user_action.startswith('show'):
        todos = functions.get_todos()
        
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index+1}-{item}')  


    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()
            new_todo = input('Introdu o alta activitate: ')
            todos[number] = new_todo + '\n'
            functions.write_todos(todos,"store.txt")

        except ValueError:
            print("Your command is not valid!")
            continue

    elif user_action.startswith('complete'):

        try:    
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            activitate_inlaturata = todos[index]
            todos.pop(index)
            functions.write_todos(todos,"store.txt")
            print(f'Activitatea {activitate_inlaturata.upper()} a fost inlaturata din lista!')

        except IndexError:
            print("Out of list range!")
            continue

    elif user_action.startswith('exit'):
        break
    
    else:
        print("Input error!")   

print('Bye!')
        
    
 