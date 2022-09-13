def Valido(solucion,etapa):
	# Comprueba si el vector solucion construido hasta la etapa es 
	# prometedor, es decir, si la reina se puede situar en la columna de la etapa

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

def backtracking(solucion, etapa, n):
    while solucion[etapa] < n:
        solucion[etapa] = solucion[etapa] + 1
        if(etapa != n-1):
            backtracking(solucion, etapa+1, n)
        elif(etapa==n-1):
            if (esSolucion(solucion,etapa)):
                print(solucion)
    solucion[etapa] = 0
    
    
    
def inicializarMetodo(n):
    solucion = []
    for i in range(n):
        solucion.append(0)
    etapa = 0
    backtracking(solucion, etapa, n)
    return solucion

def calcularNReinas():
    print ("################################################################")
    print ("Introduce el numero de reinas:")

    n = int(input())
    while(n<4):
        print("Valores incorrecto, ingrese un valor")
        n = int(input())
    
    print("Haciendo Backtracking...")
    inicializarMetodo(n)
