import os
import time
import backtracking 
import lasVegas 
import minimoConflictos

## Menu para poder elegir que algoritmo ejecutar
def opcionesText():
    os.system ("cls") 
    time.sleep(1)
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
    continuar = True
    while continuar:
            opcionesText()
            print("Introduzca un valor: ") 
            opcion = input()
            if(opcion == '1' ):
                backtracking.calcularNReinas()
            elif(opcion == '2'):
                lasVegas.calcularNReinas()
            elif(opcion == '3'):
                minimoConflictos.calcularNReinas()
            else:
                print("Hasta la proxima!...")
                continuar = False

            if continuar:
                print("Presione enter para continuar...")
                input()

menu()
