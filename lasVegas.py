import time
import random

#Variables para el tiempo de ejecucion del metodo las vegas 
tiempoMax = tiempoIteracion = 0.0

#variables para el calculo de posicion de las N reinas
columnas = dominio = []
tamanho = 0

#Variable para contar cuantos estados expandidos
estadosExpandidos = 0

def introducirDatos():
    global tamanho, tiempoMax, tiempoIteracion

    print("Introducir un valor de N: ")
    n = input()
    tamanho = int(n)

    print("Tiempo maximo de espera ( en segundos ): ")
    n = input()
    tiempoMax = float(n)

    print("Tiempo maximo de espera en cada iteracion ( en segundos ): ")
    n = input()
    tiempoIteracion = float(n)


def initNReinas():
    global tamanho,dominio,columnas
    
    # Inicializar columnas
    dominio = list(range(1,tamanho+1))
    columnas = []

def calcularNReinas():
    global dominio,columnas,tiempoMax,estadosExpandidos

    # Carga de datos
    introducirDatos()

    # Variables para controlar la finalizacion del algoritmo
    solucion = None
    inicio = fin = time.time()
    
    # Si no encuentra una solucion que pruebe con otros valores mientras aun le queda tiempo de ejecucion
    while fin - inicio < tiempoMax and solucion == None:
        # Inicio del algoritmo
        initNReinas()
        solucion = insertarReina(dominio, columnas, time.time())
        # Si se encontro una solucion
        if solucion != None:
            print(solucion)

        fin = time.time()

    if solucion == None:
        print("No se encontro una solucion")

    print("Estados explorados:",estadosExpandidos)
    print("Tiempo transcurrido : ", fin - inicio," segundos")
    

def insertarReina(dominio, columnas, inicioIteracion):

    global tiempoIteracion,estadosExpandidos

    # Caso base, ya no hay dominio, por lo tanto estan todas las reinas en una posicion valida
    if dominio == []:
        return columnas
    
    resultado = None

    # Ponemos la reina en una poscion aleatoria simpre que aun exista posiciones que no probamos anteriormente
    sinProbar = list(dominio)
    while sinProbar != [] and resultado == None:

        # Que continue probando a partir del estado inicial siempre que tenga tiempo para seguir iterando
        finIteracion = time.time()
        if finIteracion - inicioIteracion < tiempoIteracion:
            
            # poscion aleatoria
            random.seed(time.time())
            indice = random.randint(0, len(sinProbar)-1)
            posicion = sinProbar[indice]

            #Se elimina de la lista de posciones que aun no se probaron
            sinProbar.remove(posicion)

            # Contar nuevo estado explorado
            estadosExpandidos += 1

            # Verificamos que se puede insertar la reina en la posicion
            if puedeInsertar(columnas,posicion):
                # Agregamos la posicion de la nueva reina
                columnas.append(posicion)
                #  Quitamos la posicion actual del dominio para la siguiente iteracion
                dominio.remove(posicion)

                resultado = insertarReina(dominio, columnas, time.time())
                # Si no se encuentra la solucion
                if resultado == None:
                    # Volvemos a agregar la posicion que se habia quitado al dominio
                    dominio.append(posicion)
                    # Quitamos la posicion de la reina que habiamos agregado a la lista columna
                    columnas.remove(posicion)
        else:
            return None            
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