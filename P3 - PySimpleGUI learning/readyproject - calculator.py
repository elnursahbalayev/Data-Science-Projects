import PySimpleGUI as sg

bw = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':('black', '#F8F8F8')}
bt = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':('black', '#F1EABC')}
bo = {'size':(15,2), 'font':('Franklin Gothic Book', 24), 'button_color':('black', '#ECA527'), 'focus':True}

layout = [
    [sg.Text('PyDataMath-2', size=(50,1), justification='right', background_color='#272533',
             text_color='white', font=('Franklin Gothic Book', 14, 'bold'))],
    [sg.Text('0.0000', size=(18,1), justification='right', background_color='black', text_color='red',
             font=('Digital-7', 48), relief='sunken', key='-DISPLAY-')],
    [sg.Button('C', **bt), sg.Button('CE', **bt), sg.Button('%', **bt), sg.Button('/', **bt)],
    [sg.Button('7', **bt), sg.Button('8', **bt), sg.Button('9', **bw), sg.Button('*', **bt)],
    [sg.Button('4', **bt), sg.Button('5', **bt), sg.Button('6', **bw), sg.Button('-', **bt)],
    [sg.Button('1', **bt), sg.Button('2', **bt), sg.Button('3', **bw), sg.Button('+', **bt)],
    [sg.Button('0', **bt), sg.Button('.', **bt), sg.Button('=', **bo)]

]

window = sg.Window('PyDataMath-2', layout=layout, background_color='#272533', size=(580, 660))

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, None):
        break

