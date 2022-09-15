import random   
    
#clase fila, tiene la posicion de donde esta una reina en cada fila y un arreglo que representa el nro de problemas de cada casilla
class Fila:
    def __init__(self, n, columna):
        self.problema=True #saber si la fila tiene problemas
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
        self.solucion=False #variable que verifica que ya sea una solucion
        for c in range(0, n, 1):
            columna=random.randint(0, n-c-1)#random de que posicion del arreglo 
            self.filas.append(Fila(n, dominio[columna]))#el valor de fila a asignar a esta columna
            dominio.pop(columna)#descarto ese valor del dominio
            
            
    #tablero para visualizar donde se encuentran las reinas ubicadas        
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
                    print("|",1, end=" ")
            print("|")  
            
            
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
#2- MOVER SIEMPRE EN LA MISMA FILA(DONDE MENOS PROBLEMAS EXISTA OBVIO, TAMBIEN ACTUALIZAR EL NRO DE PROBLEMAS EN LA CASILLA)
#3-           
            
    #recibe de parametro el nro de fila
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
        col=columna#quita la columna del atributo columna
        #abajo hacia la derecha el movimiento
        while fil<len(self.filas) and col<len(self.filas):
            self.filas[fil].problemas[col]+=sumando
            fil+=1
            col+=1
                   
    #recibe de parametro el nro de fila    
    def verDiagSecundaria(self, fila, columna, sumando):
        fil=fila-1
        col=columna#quita la columna del atributo columna
        #arriba hacia la derecha el movimiento
        while fil>=0 and col<len(self.filas):
            self.filas[fil].problemas[col]+=sumando
            fil-=1
            col+=1
                    
        
        fil=fila+1
        col=columna-2#quita la columna del atributo columna
        #abajo hacia la izquierda el movimiento
        while fil<len(self.filas) and col>=0:
            self.filas[fil].problemas[col]+=sumando
            fil+=1
            col-=1
        
    #actualiza la concha de tu vieja
    def verColumna(self, fila, columna, sumando):
        col=columna
        for c in range(0, len(self.filas), 1):
            #actualiza toda la columna menos el elemento de la fila en intercambio de reinas
            if c!=col-1:
                self.filas[c].problemas[col]+=sumando
                   
            
    #recibe de parametro de donde viene y a donde va una reina al moverla(dentro de una fila)
    #ambos parametros -1 si es una actualizacion inicial

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
            
        #KILOMBO ACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        else:
            #aqui cuando se mueve una reina en la fila    
            #se intercambia, de donde va y de donde viene, las casillas no se alteran
            #se modifican los valores de las diagonales y las columnas respectivamente de las casillas involucradas(suma y resta)
            #el resto de los valores se mantiene
            
            self.filas[fila].columna=dondeVa #a que columna muevo la reina
            colDondeVa=self.filas[fila].columna
            
            
            #para tener la columna de donde quite
            colViene=dondeViene
            
            #actualizacion de columna y diagonales de nueva posicion, +1 para la sumar
            self.verDiagPrincipal(fila, colDondeVa, 1)
            self.verDiagSecundaria(fila, colDondeVa, 1)
            self.verColumna(fila, colDondeVa, 1)
            
            
            #actualizacion de columna y diagonales de antigua posicion, por eso -1 el parametro
            self.verDiagPrincipal(fila, colViene, -1)
            self.verDiagSecundaria(fila, colViene, -1)
            self.verColumna(fila, colViene, -1)
     
     
    def esSolucion(self):
        for c in range(0, len(self.filas), 1):
            if self.filas[c].problema==True:
                return False 
        return True
    
    
    def salidaResultado(self):
        print("[", end=" ")
        for c in range(0, len(self.filas), 1):
            print("", self.filas[c].columna, end=" ")
        print("]")    
        
          
            
            
                
                
                
                
    
        
        

