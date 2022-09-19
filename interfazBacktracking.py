import sys

from backtracking import inicializarMetodoGUI

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg


class backtrackingGUI:

    def __init__(self):
        sg.ChangeLookAndFeel('LightBlue')
        layout = [[sg.Text('Backtracking', size=(40, 1), justification='center')],
                  [sg.Text(text='Datos', justification='center')],
                  [sg.Text('Numero de reinas:')],
                  [sg.InputText()],
                  [sg.Text('Desea encontrar todas las posibles soluciones o solo la primera? 1. Todas 2. Una:')],
                  [sg.InputText()],
                  [sg.Button('Calcular', key='calcular')]
                  ]
        self.window = sg.Window('N-Reinas', location=(800, 400))
        self.window.Layout(layout).Finalize()
        estadoVentana = True
        while estadoVentana:
            event, values = self.window.Read()      #en 'values' se guarda los datos de las cajas de textos(lista)
            if event == 'Exit' or event is None:
                estadoVentana = False
            if event == 'calcular':
                if self.validar(values):
                    resultados = inicializarMetodoGUI(values[0], values[1])  
                    mostrarResultados(resultados)
                
    def validar(self, values):
        if len(values)<2:
            sg.Popup('Faltan completar datos')
            return False
        elif int(values[0])<4:
            sg.Popup('Ingrese un numero de reinas mayor a 3')
            return False
        elif int(values[1]) != 1 and int(values[1]) != 2:
            sg.Popup('Ingrese un modo de solución valido')
            return False
        else:
            return True

class mostrarResultados:
    def __init__(self, resultados):
        sg.ChangeLookAndFeel('LightBlue')
        output = sg.Output(size=(50, 10))
        layout = [[sg.Text('Resultados', size=(40, 1), justification='center')],
                  [sg.Text(text='Ubicacion de reinas:')],
                  [output]
                  ]
        self.window = sg.Window('N-Reinas', location=(800, 400))
        self.window.Layout(layout).Finalize()
        output.update(resultados)
        event = self.window.Read()      

            
        
        
