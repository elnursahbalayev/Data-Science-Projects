import PySimpleGUI as sg

sg.Print('This text is white on a green background', text_color='white', background_color='green', font='Courier 10')
sg.Print('The first call sets some window settings like font that cannot be changed')
sg.Print('This is plain text just like a print would display')
sg.Print('White on Red', background_color='red', text_color='white')
sg.Print('The other print', 'parms work', 'such as sep', sep=',')
sg.Print('To not extend a colored line use the "end" parm', background_color='blue', text_color='white', end='')
sg.Print('\nThis line has no color.')