import sys

from lasVegas import calcularNReinas

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg


class lasVegasGUI:

    def __init__(self):
        sg.ChangeLookAndFeel('LightBlue')
        layout = [[sg.Text('Algoritmo de Las Vegas', size=(40, 1), justification='center')],
                  [sg.Text(text='Datos', justification='center')],
                  [sg.Text('Numero de reinas:')],
                  [sg.InputText()],
                  [sg.Text('Tiempo maximo de espera ( en segundos ):')],
                  [sg.InputText()],
                  [sg.Text('Tiempo maximo de espera en cada iteracion ( en segundos ): ')],
                  [sg.InputText()],
                  [sg.Text('Desea encontrar la mayor cantidad de soluciones o solo una')],
                  [sg.Radio('1. Varios', "RADIO1", default=False)],
                  [sg.Radio('2. Una', "RADIO1", default=True)],
                  [sg.Button('Calcular', key='calcular')]
                  ]
        self.window = sg.Window('N-Reinas', location=(400,250))
        self.window.Layout(layout).Finalize()
        estadoVentana = True
        while estadoVentana:
            event, values = self.window.Read()      #en 'values' se guarda los datos de las cajas de textos(lista)
            print("event",event)
            if event == 'Exit' or event is None:
                estadoVentana = False
            if event == 'calcular':
                if self.validar(values):
                    if values[4]:
                        modo = 2
                    else:
                        modo = 1
                    resultados = calcularNReinas(values[0], values[1], values[2],modo)  
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
                  [sg.Text('Cantidad de soluciones:'), sg.Text(resultados[0])],
                  [sg.Text('Tiempo utilizado:'), sg.Text(resultados[3])],
                  [sg.Text('Estados expandidos:'), sg.Text(resultados[2])]
                  ]
        self.window = sg.Window('N-Reinas', location=(400,250))
        self.window.Layout(layout).Finalize()
        output.update(resultados[1])
        event = self.window.Read()