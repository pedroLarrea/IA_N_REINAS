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
                  [sg.Text('Desea encontrar todas las posibles soluciones o solo la primera?:')],
                  [sg.Radio('1. Todas', "RADIO1", default=False)],
                  [sg.Radio('2. Una', "RADIO1", default=True)],
                  [sg.Button('Calcular', key='calcular')]
                  ]
        self.window = sg.Window('N-Reinas', location=(400,250))
        self.window.Layout(layout).Finalize()
        estadoVentana = True
        while estadoVentana:
            event, values = self.window.Read()      #en 'values' se guarda los datos de las cajas de textos(lista)
            if event == 'Exit' or event is None:
                estadoVentana = False
            if event == 'calcular':
                if self.validar(values):
                    if values[1]:
                        modo = 1
                    else:
                        modo = 2
                    resultados = inicializarMetodoGUI(values[0], modo)  
                    mostrarResultados(resultados)
                
    def validar(self, values):
        if len(values)<2:
            sg.Popup('Faltan completar datos')
            return False
        elif int(values[0])<4:
            sg.Popup('Ingrese un numero de reinas mayor a 3')
            return False
        else:
            return True

class mostrarResultados:
    def __init__(self, resultados):
        sg.ChangeLookAndFeel('LightBlue')
        output = sg.Output(size=(50, 10))
        layout = [[sg.Text('Resultados', size=(40, 1), justification='center')],
                  [sg.Text(text='Ubicacion de reinas:')],
                  [output],
                  [sg.Text('Tiempo utilizado:'), sg.Text(resultados[2])],
                  [sg.Text('Estados expandidos:'), sg.Text(resultados[1])]
                  ]
        self.window = sg.Window('N-Reinas', location=(400,250))
        self.window.Layout(layout).Finalize()
        output.update(resultados[0])
        event = self.window.Read()      

            
        
        
