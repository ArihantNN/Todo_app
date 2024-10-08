import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = 'Enter to-do',key="todo")
add_button = sg.Button("Add", key = 'add')

list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size = [45,10])
edit_button = sg.Button('Edit', key = 'edit')
complete_button = sg.Button('Complete', key='complete')
exit_button = sg.Button('Exit', key = 'exit')


window = sg.Window('My To-Do App',
                   layout=[
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button, complete_button],
                       [exit_button]
                   ],
                   font = ('Helvetica', 12))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value ="")

        case "edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values = todos)
        case "todos":
            window['todo'].update(value = values['todos'][0])

        case "complete":
            completed_todo = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(completed_todo)
            functions.write_todos(todos)
            window['todos'].update(values = todos)
            window['todo'].update(value = "")
        case 'exit':
            break




        case sg.WINDOW_CLOSED:
            break


window.close()

