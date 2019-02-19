def ArbolBinario(r):
    return [r,[],[]]
def insertarIzquierdo(raiz,nuevaRama):
    t=raiz.pop(1)
    if len(t)>1:
        raiz.insert(1,[nuevaRama,t,[]])
    else:
        raiz.insert(1,[nuevaRama,[],[]])
def insertarDerecha(raiz,nuevaRama):
    t=raiz.pop(2)
    if len(t)>1:
        raiz.insert(1,[nuevaRama,t,[]])
    else:
        raiz.insert(1,[nuevaRama,[],[]])