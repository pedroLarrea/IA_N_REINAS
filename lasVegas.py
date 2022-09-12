import time
import random

#Variables para el tiempo de ejecucion del metodo las vegas 
tiempoMax = 1
inicio = fin = 0

#variables para el calculo de posicion de las N reinas
columnas = dominio = []
tamanho = solucion = continuar = 0

def introducirDatos():
    global tamanho

    print("Introducir un valor de N: ")
    n = input()
    tamanho = int(n)

def initNReinas():
    global tamanho,dominio,columnas
    
    # Inicializar columnas
    dominio = list(range(1,tamanho+1))
    columnas = []

def calcularNReinas():
    global tamanho,dominio,columnas, solucion, continuar,tiempoMax, inicio, fin

    # Carga de datos
    introducirDatos()

    # Variables para controlar la finalizacion del algoritmo
    solucion = False
    continuar = True
    inicio = time.time()
    fin = inicio

    # Inicio del algoritmo
    initNReinas()
    solucion = insertarReina(dominio,columnas)
    print(solucion)
    

def insertarReina(dominio, columnas):

    # Caso base, ya no hay dominio, por lo tanto estan todas las reinas en una posicion valida
    if dominio == []:
        return columnas
    
    resultado = None

    # Ponemos la reina en una poscion aleatoria simpre que aun exista posiciones que no probamos anteriormente
    sinProbar = list(dominio)
    while sinProbar != [] and resultado == None:
        # poscion aleatoria
        random.seed(time.time())
        indice = random.randint(0, len(sinProbar)-1)
        posicion = sinProbar[indice]

        #Se elimina de la lista de posciones que aun no se probaron
        sinProbar.remove(posicion)

        # print("Posicion Seleccionada ", posicion , "para la columna ",len(columnas)+1)

        # Verificamos que se puede insertar la reina en la posicion
        if puedeInsertar(columnas,posicion):
            # Agregamos la posicion de la nueva reina
            columnas.append(posicion)
            #  Quitamos la posicion actual del dominio para la siguiente iteracion
            dominio.remove(posicion)

            resultado = insertarReina(dominio, columnas)
            # Si no se encuentra la solucion
            if resultado == None:
                # Volvemos a agregar la posicion que se habia quitado al dominio
                dominio.append(posicion)
                # Quitamos la posicion de la reina que habiamos agregado a la lista columna
                columnas.remove(posicion)
    return resultado
    


def puedeInsertar(columnas, posicion):
    # Se recorre la lista de reinas ya insertadas para verificar si se puede insertar
    if len(columnas) > 0:
        for i in range(0,len(columnas)):
            if not verificarRestricciones(posicion, len(columnas)+1, columnas[i], i+1) :
                return False
    return True

def verificarRestricciones(fila, columna, reinaFila, reinaColumna):
    difFilas = fila - reinaFila
    difColumna = columna - reinaColumna
    div = difFilas / difColumna
    # Para determinar si no es parte de la diagonal
    if div != 1 and div != -1 :
        return True
    return False