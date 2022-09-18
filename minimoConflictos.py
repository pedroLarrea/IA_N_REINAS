from unittest import result
from minimoConflictosClases import * #archivo de clases
import time #calculo de tiempo

#funcion para definir el dominio de valores disponibles en una fila
def generarDominio(n):
    dominio=[]
    for c in range(0, n, 1):
        dominio.append(c+1)
    return dominio



def calcularNReinas(n, tiempoEspera, graficar):
    n=int(n)
    tiempoEspera=int(tiempoEspera)
    graficar=int(graficar)
    print ("--------------------------------------------------------------")
    
    #print ("Introduce el numero de reinas:")
    # Solo se puede como minimo con 4 reinas
    """n = int(input())
    while(n<4):
        print("Valores incorrecto, ingrese un valor")
        n = int(input())
    """
    #print("tiempo maximo de espera(segundos):")
    #tiempoEspera=float(input())
    
    #print("desea imprimir el tablero resultado?: 1-Si\t2-No")
    #graficar=int(input())
    

    #print("Dominio de valores: ")
    dominio=generarDominio(n)
    #print(dominio)
    
    #generacion de tablero
    tablero=Tablero(n, dominio)
    print("tablero inicial:")
    #tablero.imprimirTablero()

    #print("problemas en casillas")
    #tablero.imprimirProblemas()
    tablero.updateTableroProblemas(-1, -1, -1)#-1 ambos parametros para inicializar el tablero
    #tablero.imprimirProblemas()
    #print("longitud filas: ", len(tablero.filas))
    #tablero.imprimirProblemas()

    
    print ("--------------------------------------------------------------")
    
    tInicio = tFin = time.time()
    
    #'ciclito' de saltos y movimientos
    filaReina=tablero.seleccionarReina() #devuelve un indice
    while tFin-tInicio<tiempoEspera and tablero.esSolucion()==False:
        #hacer el proceso de movimientos
        
        
        if filaReina!=-1:
            #print("reina seleccionada: ", filaReina+1)      
            #obtiene las columnas de origen y destino del movimiento
            casillaOrigen=tablero.filas[filaReina].columna
            #print("columna origen: ", casillaOrigen)
            
            casillaDestino=tablero.verificarFila(filaReina)
            #print("columna destino: ", casillaDestino)
           
            #update de la matriz de problemas
            tablero.updateTableroProblemas(filaReina, casillaDestino, casillaOrigen)
            
            #obtenemos a que fila saltar, necesita la fila actual
            filaReina=tablero.obtenerSgteFila(filaReina)
            
            #impresiones
            #tablero.imprimirPosReinas()
            
            #tablero.imprimirTablero()
            #print("problemas en casillas")
            #tablero.imprimirProblemas()
            
        else:
            #en caso de que no tenga una fila a donde saltar, recalcular a una reina que tenga el mayor nro de problemas
            filaReina=tablero.seleccionarReina()
        
        
        tFin=time.time()
        
        """print("1-seguir\t2-cortar")
        seguir=int(input())
        if seguir==2:
            break"""
            
            
        #print ("--------------------------------------------------------------")
        
    print ("--------------------------------------------------------------")
    print("RESULTADOS:")
    if graficar==1:
        tablero.imprimirTablero()
        
    if tablero.esSolucion()==True:
        print("Estado resultado valido, tiempo consumido ", tFin-tInicio, " segundos")
    else:
        print("No se encontro resultado en el limite de tiempo")    
    
    tablero.salidaResultado()#tira tu salida
    print("cantidad de estados recorridos:")
    print(tablero.estados)
    resultados= []
    resultados.append(tablero.salidaResultado())
    resultados.append(tablero.esSolucion())
    resultados.append(tFin-tInicio)
    resultados.append(tablero.estados)
    
    return resultados
    

        
        




