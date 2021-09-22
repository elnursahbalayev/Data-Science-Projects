import PySimpleGUI as sg
import sys

if len(sys.argv) == 1:
    fname = sg.popup_get_file('Document to open')
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancel", "No Filename Supplied")
    raise SystemExit("Cancelling: No filename supllied")
else:
    sg.popup('The filename you chose was', fname)