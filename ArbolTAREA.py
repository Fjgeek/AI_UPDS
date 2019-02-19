def ArbolBinario(r):
    return [r, [], []]

def insertarIzquierdo(raiz,nuevaRama):
    t = raiz.pop(1)
    if len(t) > 1:
        raiz.insert(1,[nuevaRama,t,[]])
    else:
        raiz.insert(1,[nuevaRama, [], []])
    return raiz

def insertarDerecho(raiz,nuevaRama):
    t = raiz.pop(2)
    if len(t) > 1:
        raiz.insert(2,[nuevaRama,[],t])
    else:
        raiz.insert(2,[nuevaRama,[],[]])
    return raiz

def obtenerValorRaiz(raiz):
    return raiz[0]

def asignarValorRaiz(raiz,nuevoValor):
    raiz[0] = nuevoValor

def obtenerHijoIzquierdo(raiz):
    return raiz[1]

def obtenerHijoDerecho(raiz):
    return raiz[2]
pino=ArbolBinario("root")
insertarDerecho(pino,"dos")
insertarIzquierdo(pino,"uno")
l1=obtenerHijoIzquierdo(pino)
insertarIzquierdo(l1,"uno.uno")
insertarDerecho(l1,"uno.dos")
r1=obtenerHijoDerecho(pino)
insertarDerecho(r1,"dos.dos")
insertarIzquierdo(r1,"dos.uno")
l1_2=obtenerHijoIzquierdo(l1)
insertarIzquierdo(l1_2,"uno.uno.uno")
insertarDerecho(l1_2,"uno.uno.dos")
l1_l2=obtenerHijoDerecho(l1)
insertarIzquierdo(l1_l2,"uno.dos.uno")
insertarDerecho(l1_l2,"uno.dos.dos")
r1_l2=obtenerHijoIzquierdo(r1)
insertarIzquierdo(r1_l2,"dos.uno.uno")
insertarDerecho(r1_l2,"dos.uno.dos")
r1_r2=obtenerHijoDerecho(r1)
insertarIzquierdo(r1_r2,"dos.dos.uno")
insertarDerecho(r1_r2,"dos.dos.dos")

#IMPRIMIENDO EL ARBOL
print (pino)

##insertar la altura

