import random
from xmlrpc.client import MAXINT, MININT   
    
#clase fila, tiene la posicion de donde esta una reina en cada fila y un arreglo que representa el nro de problemas de cada casilla
class Fila:
    def __init__(self, n, columna):
        #self.problema=True #saber si la fila tiene problemas
        self.columna=columna    #int, representa el numero de columna
        self.problemas=[]
        for c in range(0, n, 1):
            if self.columna != c+1:
                self.problemas.append(1)
            else:
                self.problemas.append(0)

            

                
            
#defino como un arreglo de la clase Fila el tablero
class Tablero:    

    def __init__(self, n, dominio):
        self.filas=[]
        for c in range(0, n, 1):
            self.estados=1                                  #contabiliza el numero de estados que se expandio el tablero
            columna=random.randint(0, n-c-1)                #random de que posicion del arreglo 
            self.filas.append(Fila(n, dominio[columna]))    #el valor de columna a asignar a esta fila
            dominio.pop(columna)                            #descarto ese valor del dominio
            
            
    #imprime el tablero con las reinas distribuidas      
    def imprimirTablero (self):
        n=len(self.filas)
        print("columna: ")
        for i in range(0, n, 1):
            print("")
            print(self.filas[i].columna, end="\t")
            for j in range(0, n, 1):
                if self.filas[i].columna!=j+1:
                    print("|",0, end=" ")#hace que el caracter final no sea \n
                else:
                    print("|",'X', end=" ")
            print("|")  
            
            
    #imprime una representacion de una dimension de las reinas        
    def imprimirPosReinas(self):
        print("[", end=" ")
        for c in range(0, len(self.filas), 1):
            print(" ", self.filas[c].columna, end=" ")
        
        print("]")    
          
            
    #funcion para imprimir un tablero donde se numeran los conflictos de cada casilla
    def imprimirProblemas (self):
        n=len(self.filas)
        print("linea de ubicacion en columnas de las reinas:")
        for c in range(0, n, 1):
            print("",int(self.filas[c].columna), end=" ")
        
        print("")
            
        print("tablero con el nro de problemas de cada casilla:")    
        for i in range(0, n, 1):
            print("")
            for j in range(0, n, 1):
                print("|",int(self.filas[i].problemas[j]), end=" ")
            print("|")
        
            
        
            
      
            
            

#ANOTACIONES
#1- VERIFICAR LOS PROBLEMAS EN LAS DIAGONALES
#2- MOVER SIEMPRE EN LA MISMA FILA(donde menos problemas existan, tambien actualizar el problemas de las casillas)
#3- AL MOVER LAS REINAS EN LAS FILAS, LOS VALORES DE LA FILA NO CAMBIAN(pueden cambiar cuando se actualiza una diagonal)
        
        
    #funcion que actualiza la diagonal principal de una reina        
    #recibe de parametro el nro de fila; sumando=1 si suma, -1 caso contrario
    def verDiagPrincipal(self, fila, columna, sumando):
        #valores iniciales
        fil=fila-1 #-1 pq el dominio va de 0 a n-1; le resto entonces 1 nomas
        col=columna-2#quita la columna del atributo columna; -2 pq el dominio de columna va de 1 a n(-1 ajuste, -1 )
        #arriba hacia la izquierda el movimiento
        while fil>=0 and col>=0:
            self.filas[fil].problemas[col]+=sumando
            fil-=1
            col-=1
                   
        #valores iniciales de nuevo
        fil=fila+1
        col=columna
        #abajo hacia la derecha el movimiento
        while fil<len(self.filas) and col<len(self.filas):
            self.filas[fil].problemas[col]+=sumando
            fil+=1
            col+=1
    
    #funcion que actualiza la diagonal secundaria de una reina               
    #recibe de parametro el nro de fila; sumando=1 si suma, -1 caso contrario   
    def verDiagSecundaria(self, fila, columna, sumando):
        fil=fila-1
        col=columna
        #arriba hacia la derecha el movimiento
        while fil>=0 and col<len(self.filas):
            self.filas[fil].problemas[col]+=sumando
            fil-=1
            col+=1
                    
        
        fil=fila+1
        col=columna-2
        #abajo hacia la izquierda el movimiento
        while fil<len(self.filas) and col>=0:
            self.filas[fil].problemas[col]+=sumando
            fil+=1
            col-=1
        
    #la funcion actualiza el nro de problemas de una reina dada
    def verColumna(self, fila, columna, sumando):
        col=columna-1
        for c in range(0, len(self.filas), 1):
            #actualiza toda la columna menos el elemento de la fila en intercambio de reinas
            if c!=fila:
                self.filas[c].problemas[col]+=sumando
                   
            
    #recibe de parametro de donde viene y a donde va una reina al moverla(dentro de una fila)
    #todos los parametros -1 si es una actualizacion inicial

    #parametros para mover dentro de la misma fila
    def updateTableroProblemas (self, fila, dondeVa, dondeViene):
        n=len(self.filas)
        if dondeVa==-1 and dondeViene==-1:
            #inicializacion de la tabla
            for c in range(0, n, 1):
                col=self.filas[c].columna
                #tiene que sumar los problemas por reinas en diagonal, por eso 1
                self.verDiagPrincipal(c, col, 1)
                self.verDiagSecundaria(c, col, 1)
            
        else:
            #aqui cuando se mueve una reina en la fila    
            #se intercambia, de donde va y de donde viene, las casillas no se alteran
            #se modifican los valores de las diagonales y las columnas respectivamente de las casillas involucradas(suma y resta)
            #el resto de los valores se mantiene
            
            self.filas[fila].columna=dondeVa #a que columna muevo la reina
            colDondeVa=self.filas[fila].columna
            
            #como aqui se movio ya una reina(se cambio su columna), el estado es diferente, se cuenta
            self.estados+=1
            
            
            
            
            #para tener la columna de donde quite
            colViene=dondeViene
            
            #actualizacion de columna y diagonales de nueva posicion, +1 para la suma
            self.verDiagPrincipal(fila, colDondeVa, 1)
            self.verDiagSecundaria(fila, colDondeVa, 1)
            self.verColumna(fila, colDondeVa, 1)
            
            
            #actualizacion de columna y diagonales de antigua posicion, por eso -1 el parametro, se resta
            self.verDiagPrincipal(fila, colViene, -1)
            self.verDiagSecundaria(fila, colViene, -1)
            self.verColumna(fila, colViene, -1)
            
            
     
    #verifica que tenga solucion 
    def esSolucion(self):
        for c in range(0, len(self.filas), 1):
            #si en la posicion en donde se encuentra la reina hay 0 problemas, esa reina tiene 0
            col=self.filas[c].columna-1
            if self.filas[c].problemas[col]!=0:
                return False 
        return True
    
    #retorna el resultado final(imprime)
    def salidaResultado(self):
        print("[", end=" ")
        for c in range(0, len(self.filas), 1):
            print("", self.filas[c].columna, end=" ")
        print("]")
        
    #busca la reina con mas problemas
    def seleccionarReina(self):
        max=0
        arregloPosibles=[]                                          #arreglo que guarda los indice que tengan el valor minimo, en caso de que existan varios
        for c in range(0, len(self.filas), 1):
            col=self.filas[c].columna-1                             
            if(self.filas[c].problemas[col]==max and max!=0):       #no tiene que agregar el que tiene 0 problemas
                arregloPosibles.append(c)
            elif(self.filas[c].problemas[col]>max):                 #si hay uno mayor, se vacia el arreglo y se agrega
                max=self.filas[c].problemas[col]
                arregloPosibles=[]
                arregloPosibles.append(c)
          
        if len(arregloPosibles)!=0:
            #random de las reinas[indice] que me vinieron, en caso de que tengan mismo numero de problemas
            nroRand=random.randint(0, len(arregloPosibles)-1)
            return arregloPosibles[nroRand]                         #retorna la fila con la reina con mas problemas
        else:
            return -1
                
        
    
    #retorna a donde mover(columna)
    def verificarFila(self, fila):
        arregloPosibles=[]                                          #arreglo que guarda los indice que tengan el valor minimo, en caso de que existan varios
        col=self.filas[fila].columna-1
        minValor=self.filas[fila].problemas[col]                    #indice del menor, de inicio es la misma columna
        posReina=self.filas[fila].columna-1                         #no evalua la posicion en la que se encuentra la reina
        for c in range(0, len(self.filas), 1):
            #casillas que posean menor o igual de problemas y que no se evalue a si mismo
            if(self.filas[fila].problemas[c]==minValor and c!=posReina):
                arregloPosibles.append(c)
            elif(self.filas[fila].problemas[c]<minValor and c!=posReina):       #reset del arreglo en caso de que exista un menor valor
                minValor=self.filas[fila].problemas[c]
                arregloPosibles=[]
                arregloPosibles.append(c)
                
                
        if len(arregloPosibles)!=0:                                 #si no es vacio retorna un indice aleatorio
            #random de las posibles columnas(el indice de los que tiene  valores iguales)
            nroRandom=random.randint(0, len(arregloPosibles)-1)
            return arregloPosibles[nroRandom]+1
        else:
            return col+1              #si no, retorna el valor que vino como parametro y no pasa nada
    
    
    #busca la siguiente fila en una columna, cuando se mueve una reina en una columna existen 2 reinas, por lo tanto hay que ir a la sgte reina para moverla
    def obtenerSgteFila(self, fila):
        columna=self.filas[fila].columna
        for c in range(0, len(self.filas), 1):
            if self.filas[c].columna==columna and c!=fila:
                return c
            
        return -1     
        

        
            
        
          
            
            
                
                
                
                
    
        
        

