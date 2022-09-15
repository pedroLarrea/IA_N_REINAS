from minimoConflictosClases import * #archivo de clases

#funcion para definir el dominio de valores disponibles en una fila
def generarDominio(n):
    dominio=[]
    for c in range(0, n, 1):
        dominio.append(c+1)
    return dominio



def main():
    print("ingrese valor de n:")
    n=int(input())
    print("dominio valores: ")
    dominio=generarDominio(n)
    print(dominio)
    

    tablero=Tablero(n, dominio)
    print("tablero:")
    tablero.imprimirTablero()

    print("problemas en casillas")
    #tablero.imprimirProblemas()
    tablero.updateTableroProblemas(-1, -1)#-1 ambos parametros para inicializar el tablero
    tablero.imprimirProblemas()
    #print("longitud filas: ", len(tablero.filas))
    #tablero.imprimirProblemas()
    #print("wtf")


    
    

main()
        
        
        
        




