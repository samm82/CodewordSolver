# GUI.py
# 3/30/2019

import PySimpleGUI as sg

def entryGUI(length, width):
    entryLayout = []

    # code from MikeyB from StackOverflow
    for i in range(width):
        line = [sg.InputText('', size=(3, 1)) for i in range(length)]
        entryLayout.append(line)
    
    entryLayout.append([sg.CloseButton("OK"), sg.CloseButton("Cancel")])

    entryWin = sg.Window("CodeWord Solver").Layout(entryLayout)
    button, values = entryWin.Read()

    if button != "OK":
        exit()
    else:
        return values
