import sys

from minimoConflictos import calcularNReinas

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
class interfazResultado:
    def __init__(self, resultados):
        sg.ChangeLookAndFeel('LightBlue')
        layout = [[sg.Text('Resultados', size=(40, 1), justification='center')],
                  [sg.Text(text='Ubicacion de reinas:')],
                  [sg.Text(text=resultados[0])],
                  [sg.Text('Es valido?:'), sg.Text(resultados[1])],
                  [sg.Text('Tiempo utilizado:'), sg.Text(resultados[2])],
                  [sg.Text('Estados recorridos:'), sg.Text(resultados[3])]
                  ]
        self.window = sg.Window('N-Reinas', location=(800, 400))
        self.window.Layout(layout).Finalize()
        while True:
            event, values = self.window.Read()      #en 'values' se guarda los datos de las cajas de textos(lista)
            if event == 'Exit' or event is None:
                sys.exit()
                break

            
        
        
