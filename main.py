import functions

while True:

    user_action = input("Type add, show, edit, done or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
            todo = user_action[4:]

            todos = functions.get_todos('todos.txt')
            todos.append(todo + '\n')

            functions.write_todos('todos.txt', todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos('todos.txt')

        for index, item in enumerate(todos):
            print(f"{index+1}-{item}", end="")


    elif user_action.startswith('edit'):
        try:
            edit_todo_num = int(user_action[5:])
            edit_todo_num -= 1

            todos = functions.get_todos('todos.txt')

            new_todo = input('Enter new todo : ')
            todos[edit_todo_num] = new_todo + '\n'

            functions.write_todos('todos.txt', todos)

        except ValueError:
            print('Your command is not valid')
            continue
    elif user_action.startswith('complete'):
        try:
            todo_completed_no = int(user_action[9:])
            todos = functions.get_todos('todos.txt')
            todo_completed = todos[todo_completed_no-1].strip('\n')
            todos.pop(todo_completed_no-1)

            functions.write_todos('todos.txt', todos)

            message = f"todo '{todo_completed}' was removed from the list"
            print(message)
        except IndexError:
            print('There is no item with that number')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Invalid input')


