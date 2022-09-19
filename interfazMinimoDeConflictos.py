import sys

from minimoConflictos import calcularNReinas

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg


class minimoDeConflictosGUI:

    def __init__(self):
        print("minimo")
        sg.ChangeLookAndFeel('LightBlue')
        layout = [[sg.Text('Minimo de conflictos', size=(40, 1), justification='center')],
                  [sg.Text(text='Datos', justification='center')],
                  [sg.Text(text='Numero de reinas:')],
                  [sg.InputText()],
                  [sg.Text('Tiempo maximo de espera ( en segundos ):')],
                  [sg.InputText()],
                  [sg.Text('Desea imprimir la tabla?:')],
                  [sg.InputText()],
                  [sg.Button('Calcular', key='calcular')]
                  ]
        self.window = sg.Window('N-Reinas', location=(800, 400))
        self.window.Layout(layout).Finalize()
        estadoVentana = True
        while estadoVentana:
            event, values = self.window.Read()
            if event == 'Exit' or event is None:
                estadoVentana = False
            if event == 'calcular':
                if self.validar(values):
                    resultados=calcularNReinas(values[0], values[1], values[2])  
                    mostrarResultados(resultados)

    def validar(self, values):
        if len(values)<3:
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
                  [sg.Text('Resultado valido:'), sg.Text(resultados[1])],
                  [sg.Text('Tiempo utilizado:'), sg.Text(resultados[2])],
                  [sg.Text('Estados recorridos:'), sg.Text(resultados[3])]
                  ]
        self.window = sg.Window('N-Reinas', location=(800, 400))
        self.window.Layout(layout).Finalize()
        output.update(resultados[0])
        event = self.window.Read()      

            
        
        
