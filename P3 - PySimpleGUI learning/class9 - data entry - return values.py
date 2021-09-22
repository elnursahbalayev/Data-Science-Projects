import PySimpleGUI as sg

sg.theme('Topanga')

layout = [[sg.Text('Please enter your Name, Address, Phone')],
          [sg.Text('Name', size=(15,1)), sg.In()],
          [sg.T('Address',size=(15,1)), sg.In()],
          [sg.T('Phone',size=(15,1)), sg.In()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Simple data entry window', layout)

event, values = window.read()

window.close()


print(event, values[0], values[1], values[2])