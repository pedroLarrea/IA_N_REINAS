import sys
from interfazResultados import interfazResultado

from minimoConflictos import calcularNReinas

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
class interfaz:
    def __init__(self):
        sg.ChangeLookAndFeel('LightBlue')
        layout = [[sg.Text('Opciones', size=(40, 1), justification='center')],
                  [sg.Text(text='Datos', justification='center')],
                  [sg.Text(text='Numero de reinas')],
                  [sg.InputText()],
                  [sg.Text('Tiempo de espera en segundos')],
                  [sg.InputText()],
                  [sg.Text('Desea imprimir la tabla? 1-Si   2-No:')],
                  [sg.InputText()],
                  [sg.Button('Calcular', key='calcular'), sg.Button('Salir', key = 'salir')]
                  ]
        self.window = sg.Window('N-Reinas', location=(800, 200))
        self.window.Layout(layout).Finalize()
        while True:
            event, values = self.window.Read()      #en 'values' se guarda los datos de las cajas de textos(lista)
            if event == 'Exit' or event is None:
                sys.exit()
                break
            if event == 'calcular':
                if self.validar(values):
                    resultados=calcularNReinas(values[0], values[1], values[2])  
                    interfazResultado(resultados)
            if event == 'salir':
                sys.exit()
    def validar(self, values):
        if len(values)<3:
            sg.Popup('Faltan completar datos')
            return False
        elif int(values[0])<4:
            sg.Popup('Ingrese un numero de reinas mayor a 3')
            return False
        else:
            return True
        
        
        
inter = interfaz()