import functions
import PySimpleGUI as sg
import time

sg.theme("DarkPurple4")
 
ceas = sg.Text('', key = 'ceas')
label = sg.Text("Introdu o activitate!")
input_box = sg.InputText(tooltip="Introdu o activitate!", key = "activitate")
add_button = sg.Button("Adauga")
list_box = sg.Listbox(values = functions.get_todos(), key = "activitati",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Editeaza")
complete_button = sg.Button("Indeplinit")
exit_button = sg.Button("Iesire")
 

layout = [[ceas],
          [label], 
          [input_box, add_button], 
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('Lista mea de activități!', layout=layout, font=('Helvetica', 20))                   

while True:
    event, values = window.read(timeout=200)
    window['ceas'].update(value=time.strftime("%b %d,%Y %H:%M:%S"))
    match event:
        case "Adauga":
            todos = functions.get_todos()
            activitate_noua = values['activitate'] + "\n"
            todos.append(activitate_noua)
            functions.write_todos(todos)
            window['activitati'].update(values=todos)
        case "Editeaza":
            try:    
                activitate_de_editat = values["activitati"][0]
                activitate_noua = values["activitate"] + "\n"
                todos = functions.get_todos()
                index = todos.index(activitate_de_editat)
                todos[index] = activitate_noua
                functions.write_todos(todos)
                window['activitati'].update(values=todos)
            except IndexError:
                sg.popup("Selecteaza o activitate de editat!", font =("Helvetica", 20))

        case 'Indeplinit':
            try:
                activitate_finalizata = values["activitati"][0]
                todos = functions.get_todos()
                todos.remove(activitate_finalizata)
                functions.write_todos(todos)
                window['activitati'].update(values=todos)
                window['activitate'].update(value='')
            except IndexError:
                sg.popup("Selecteaza o activitate de inlaturat!", font =("Helvetica", 20))
        case "Iesire":
            break
        case 'activitati':
            window['activitate'].update(value=values["activitati"][0])
        case sg.WIN_CLOSED:
            break
window.close()