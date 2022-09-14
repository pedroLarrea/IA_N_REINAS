import os
import time
import backtracking 
import lasVegas 
import minimoConflictos

## Menu para poder elegir que algoritmo ejecutar
def opcionesText():
    os.system ("cls") 
    time.sleep(2)
    #os.system ("clear") Para linux
    print ("--------------------------------------------------------------")
    print("==== INTELIGENCIA ARTIFICIAL ====\n")
    print("N - REINAS\n")   
    print("Opciones:\n")
    print("1 - Backtracking\n")     
    print("2 - Algoritmo de Las Vegas\n") 
    print("3 - Mínimo de conflictos\n")
    print("OTRO - Salir\n")   
    print ("--------------------------------------------------------------")

def menu():
    opcion = 0
    while opcion != -1:
            opcionesText()
            print("Introduzca un valor: ") 
            opcion = input()
            if(opcion == '1' ):
                backtracking.calcularNReinas()
                opcion = -1
            elif(opcion == '2'):
                lasVegas.calcularNReinas()
                opcion = -1
            elif(opcion == '3'):
                minimoConflictos.calcularNReinas()
                opcion = -1
            else:
                print("No se ha seleccionado ninguna opcion...")
                opcion = -1

menu()
