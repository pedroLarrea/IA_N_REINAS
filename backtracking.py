def Valido(solucion,etapa):
	# Comprueba si el vector solucion construido hasta la etapa cumple con las validaciones del juego
	for i in range(etapa):
		if(  ( solucion[i] == solucion[etapa]) or (ValAbs(solucion[i],solucion[etapa])==ValAbs(i,etapa) )  ):
			return False
	return True

def ValAbs(x,y):
	if x>y:
		return x - y
	else:
		return y - x	

def esSolucion(solucion,etapa):
    i = 0
    resp = True
    while(i<=etapa):
        if (not Valido(solucion,i)):
            resp = False
        i=i+1
    return resp

def imprimirFormateado(solucion,n):
    print(solucion)
    for x in range(n):
        for i in range(n):
            if solucion[x] == i+1:
                print ("X", end=" ")
            else:
                print ("--", end=" ")
        print ("\n")
    print ("\n")
    
def backtracking(solucion, etapa, n, primerResult, encontrado):
    response = True
    while solucion[etapa] < n:
        solucion[etapa] = solucion[etapa] + 1
        if(etapa != n-1):
            if (not backtracking(solucion, etapa+1, n, primerResult, encontrado)):
                encontrado = True
                break
        elif(etapa==n-1):
            if (esSolucion(solucion,etapa)):
                #Si solo se busca el primer resultado
                if(primerResult and encontrado==False):
                    encontrado = True
                    imprimirFormateado(solucion,n)
                    break
                else:
                    imprimirFormateado(solucion,n)
    solucion[etapa] = 0
    if(primerResult and encontrado):
        response = False
    return response
    
    
    
def inicializarMetodo(n, modo):
    solucion = []
    for i in range(n):
        solucion.append(0)
    etapa = 0
    if(modo == 1):
        #Todas las posibles opciones
        backtracking(solucion, etapa, n, False, False)
    else:
        #Una sola opcion
        backtracking(solucion, etapa, n, True, False)
    return solucion

def calcularNReinas():
    print ("--------------------------------------------------------------")
    print ("Introduce el numero de reinas:")

    n = int(input())
    while(n<4):
        print("Valores incorrecto, ingrese un valor")
        n = int(input())
    
    print("Desea encontrar todas las posibles soluciones o solo la primera? 1. Todas 2. Una Otro. incorrecto")
    modo = int(input())
    while(not (modo== 1 or modo==2)):
        print("Debe ingresar una opcion valida: 1 o 2")
        modo = int(input())
        
    print("Haciendo Backtracking...")
    inicializarMetodo(n, modo)
