import PySimpleGUI as sg

choices = ('Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Chartreuse')

layout = [[sg.T('What is your favourite color?')],
          [sg.LB(choices, size=(15,len(choices)), key='-COLOR-')],
          [sg.B('Ok')]]

window = sg.Window('Pick a color', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Ok':
        if values['-COLOR-']:
            sg.popup(f"Your favourite color is {values['-COLOR-'][0]}")

window.close()