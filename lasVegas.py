import time
import random
import sys

#Variables para el tiempo de ejecucion del metodo las vegas 
tiempoMax = tiempoIteracion = 0.0

#Para determinar cantidad de resultados esperados
modo = 0

#variables para el calculo de posicion de las N reinas
columnas = dominio = []
tamanho = 0

#Variable para contar cuantos estados expandidos
estadosExpandidos = 0

#Para determinar si graficar o no
graficar = 0

def introducirDatos():
    global tamanho, tiempoMax, tiempoIteracion, modo, graficar

    print ("--------------------------------------------------------------")
    print ("Introduce el numero de reinas:")
    
    # Solo se puede como minimo con 4 reinas
    n = int(input())
    while(n<4):
        print("Valores incorrecto, ingrese un valor")
        n = int(input())

    tamanho = n

    sys.setrecursionlimit(2000)

    print("Tiempo maximo de espera ( en segundos ): ")
    n = input()
    tiempoMax = float(n)

    print("Tiempo maximo de espera en cada iteracion ( en segundos ): ")
    n = input()
    tiempoIteracion = float(n)

    print("Desea encontrar la mayor cantidad de soluciones en", tiempoMax ,"segundos o solo una? 1. Todas 2. Una Otro. incorrecto")
    modo = int(input())
    while(not (modo== 1 or modo==2)):
        print("Debe ingresar una opcion valida: 1 o 2")
        modo = int(input())

    print("Desea graficar las soluciones encontradas? 1. Si 2. No. Otro. incorrecto")
    graficar = int(input())
    while(not (graficar== 1 or graficar==2)):
        print("Debe ingresar una opcion valida: 1 o 2")
        graficar = int(input())


def initNReinas():
    global tamanho,dominio,columnas
    
    # Inicializar columnas
    dominio = list(range(1,tamanho+1))
    columnas = []

def calcularNReinas():
    global dominio,columnas,tiempoMax,estadosExpandidos, modo

    # Carga de datos
    introducirDatos()

    # Variables para controlar la finalizacion del algoritmo
    sinSolucion = True
    solucion = None
    inicio = fin = time.time()
    cantidadSoluciones = 0
    solucionesEncontradas = []

    # Si no encuentra una solucion que pruebe con otros valores mientras aun le queda tiempo de ejecucion
    while fin - inicio < tiempoMax and solucion == None:
        # Inicio del algoritmo
        initNReinas()
        tiempo = time.time()
        solucion = insertarReina(dominio,dominio, columnas, tiempo)
        # Si se encontro una solucion y no es repetida
        if solucion != None and solucion not in solucionesEncontradas:
            # Agregar a la lista de respuestas conocidas
            solucionesEncontradas.append(solucion)

            # Cantidad de respuestas encontradas
            cantidadSoluciones += 1

            # Imprimir solucion
            imprimirFormateado(solucion,len(solucion))

            # Bandera para verificar si se ha encontrado una solucion
            sinSolucion = False
        
        # Para continuar con la ejecucion si es que elegio 'Todas'
        if solucion != None and modo == 1:
            solucion = None

        fin = time.time()

    if sinSolucion:
        print("No se encontro una solucion")
    else:
        print("Se han encontrado: ",cantidadSoluciones)

    print("Estados explorados:",estadosExpandidos)
    print("Tiempo transcurrido : ", fin - inicio," segundos")
    

def insertarReina(dominioLocal, dominio, columnas, inicioIteracion):

    global tiempoIteracion,estadosExpandidos

    # Caso base, ya no hay dominio, por lo tanto estan todas las reinas en una posicion valida
    if dominio == []:
        return columnas
    
    resultado = None

    # Ponemos la reina en una poscion aleatoria simpre que aun exista posiciones que no probamos anteriormente
    sinProbar = list(dominioLocal)
    while sinProbar != [] and resultado == None:

        # Que continue probando a partir del estado inicial siempre que tenga tiempo para seguir iterando
        finIteracion = time.time()
        if finIteracion - inicioIteracion < tiempoIteracion:
            
            # poscion aleatoria
            random.seed(time.time())
            if len(sinProbar) > 1:
                indice = random.randint(0, len(sinProbar)-1)
            else:
                indice = 0
            posicion = sinProbar[indice]

            #Se elimina de la lista de posciones que aun no se probaron
            sinProbar.remove(posicion)

            # Contar nuevo estado explorado
            estadosExpandidos += 1

            # Agregamos la posicion de la nueva reina
            columnas.append(posicion)
            #  Quitamos la posicion actual del dominio para la siguiente iteracion
            dominio.remove(posicion)

            nextDominio = calcularDominioSiguiente(dominio,columnas)

            resultado = insertarReina(nextDominio,dominio, columnas, time.time())
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

def calcularDominioSiguiente(Dominio, Columnas):
    nextDominio = list(Dominio)
    for id,d in enumerate(Columnas):
        nextDominio = calcularIntersecciones(d,id+1,len(Columnas)+1,nextDominio)
    return nextDominio;


def calcularIntersecciones(FilaConocida,ColumnaConocida,Columna,Dominio): 
    interseccion1 = Columna - ColumnaConocida + FilaConocida
    if interseccion1 in Dominio:
        Dominio.remove(interseccion1)
    interseccion2 = ColumnaConocida - Columna + FilaConocida
    if interseccion2 in Dominio:
        Dominio.remove(interseccion2)
    if FilaConocida in Dominio:
        Dominio.remove(FilaConocida)
    return Dominio

def verificarRestricciones(fila, columna, reinaFila, reinaColumna):
    difFilas = fila - reinaFila
    difColumna = columna - reinaColumna
    div = difFilas / difColumna
    # Para determinar si no es parte de la diagonal
    if div != 1 and div != -1 :
        return True
    return False


def imprimirFormateado(solucion,n):
    global graficar
    print(solucion)
    if graficar == 1:
        for x in range(n):
            for i in range(n):
                if solucion[i] == x+1:
                    print ("X", end=" ")
                else:
                    print ("--", end=" ")
            print ("\n")
        print ("\n")