from minimoConflictosClases import * #archivo de clases

#funcion para definir el dominio de valores disponibles en una fila
def generarDominio(n):
    dominio=[]
    for c in range(0, n, 1):
        dominio.append(c+1)
    return dominio



def calcularNReinas():
    print ("--------------------------------------------------------------")
    print ("Introduce el numero de reinas:")
    n=int(input())

    #print("Dominio de valores: ")
    dominio=generarDominio(n)
    #print(dominio)
    
    tablero=Tablero(n, dominio)
    print("tablero:")
    tablero.imprimirTablero()

    print("problemas en casillas")
    tablero.imprimirProblemas()
    tablero.updateTableroProblemas(-1, -1, -1)#-1 ambos parametros para inicializar el tablero
    tablero.imprimirProblemas()
    #print("longitud filas: ", len(tablero.filas))
    #tablero.imprimirProblemas()

    
    print ("--------------------------------------------------------------")
    
    #'ciclito' de saltos y movimientos
    filaReina=tablero.seleccionarReina() #devuelve un indice
    while tablero.esSolucion()==False:
        #hacer el proceso de movimientos
        
        
        if filaReina!=-1:
            print("reina seleccionada: ", filaReina+1)      
            #obtiene las columnas de origen y destino del movimiento
            casillaOrigen=tablero.filas[filaReina].columna
            print("columna origen: ", casillaOrigen)
            
            casillaDestino=tablero.verificarFila(filaReina)
            print("columna destino: ", casillaDestino)
           
            #update de la matriz de problemas
            tablero.updateTableroProblemas(filaReina, casillaDestino, casillaOrigen)
            #obtenemos a que fila saltar, necesita la fila actual
            filaReina=tablero.obtenerSgteFila(filaReina)
            print("tablero")
            tablero.imprimirTablero()
            print("problemas en casillas")
            tablero.imprimirProblemas()
            
        else:
            #en caso de que no tenga una fila a donde saltar, recalcular a una reina que tenga el mayor nro de problemas
            filaReina=tablero.seleccionarReina()
        
        
        """print("1-seguir\t2-cortar")
        seguir=int(input())
        if seguir==2:
            break"""
        print ("--------------------------------------------------------------")
        
    print ("--------------------------------------------------------------")
    tablero.imprimirProblemas()
    print("resultado de la busqueda:")
    tablero.salidaResultado()#tira tu salida

        
        
calcularNReinas()



