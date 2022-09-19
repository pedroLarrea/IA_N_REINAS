import os
import time
import backtracking 
import lasVegas 
import minimoConflictos
import sys
from interfazMinimoDeConflictos import minimoDeConflictosGUI
from interfazLasVegas import lasVegasGUI
from interfazBacktracking import backtrackingGUI

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

## Menu para poder elegir que algoritmo ejecutar
class mainGUI:

    def __init__(self):
        sg.ChangeLookAndFeel('LightBlue')
        layout = [
                  [sg.Text('Problema de las N Reinas', size=(40, 1), justification='center')],
                  [sg.Text(text='Seleccione una opción:', justification='center')],
                  [sg.Button('Backtracking', key='backtrackingBtn')],
                  [sg.Button('Algoritmo de Las Vegas', key='lasVegasBtn')],
                  [sg.Button('Mínimo de conflictos', key='minimoConflictosBtn')],
                  [sg.Button('Salir', key = 'salir')]
                  ]
        self.window = sg.Window('N-Reinas', location=(800, 400))
        self.window.Layout(layout).Finalize()
        while True:
            event, values = self.window.Read()
            if event == 'Exit' or event is None:
                sys.exit()
                break
            if event == 'minimoConflictosBtn':
                minimoDeConflictosGUI() 
            if event == 'lasVegasBtn':
                lasVegasGUI()
            if event == 'backtrackingBtn':
                backtrackingGUI()
            if event == 'salir':
                sys.exit()

menu = mainGUI()
