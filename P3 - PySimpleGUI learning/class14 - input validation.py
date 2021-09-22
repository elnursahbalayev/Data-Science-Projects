import PySimpleGUI as sg

"""
    Restrict the characters allowed in an input element to digits and . or -
    Accomplished by removing last character input if not a valid character
"""

layout = [[sg.Text('Input only floating point numbers')],
          [sg.Input(key='-IN-', enable_events=True)],
          [sg.Button('Exit')]]

window = sg.Window('Floating point input valudation', layout, location=(500, 300), size=(500,300))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-IN-' and values['-IN-'] and values['-IN-'][-1] not in ('0123456789.-'):
        window['-IN-'].update(values['-IN-'][:-1])

window.close()