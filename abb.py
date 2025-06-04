from dataclasses import dataclass

@dataclass
class Abb:
    dato: int
    hijo_izq: 'Abb | None' = None
    hijo_der: 'Abb | None' = None

def creaAbbUnitario(valor: int) -> Abb:
    return(Abb(valor))

def esAbbVacio(arbol: Abb | None) -> bool:
    if(arbol == None):
        return(True)
    else:
        return(False)

def buscaValorAbb(arbol: Abb | None, valor: int) -> Abb:
    if(arbol == None):
        return(None)
    elif(valor < arbol.dato):
        return(buscaValorAbb(arbol.hijo_izq, valor))
    elif(valor > arbol.dato):
        return(buscaValorAbb(arbol.hijo_der, valor))
    return(arbol)

def insertaValorAbb(arbol: Abb | None, valor: int ) -> Abb:
    if(arbol == None):
        arbol = creaAbbUnitario(valor)
    elif(valor < arbol.dato):
        arbol.hijo_izq = insertaValorAbb(arbol.hijo_izq, valor)
    elif(valor > arbol.dato):
        arbol.hijo_der = insertaValorAbb(arbol.hijo_der, valor)
    return(arbol)

def eliminaValorAbb(arbol: Abb | None, valor: int ) -> Abb:
    if(arbol == None):
        return(None)
    elif(valor < arbol.dato):
        arbol.hijo_izq = eliminaValorAbb(arbol.hijo_izq, valor)
    elif(valor > arbol.dato):
        arbol.hijo_der = eliminaValorAbb(arbol.hijo_der, valor)
    else:
        if((arbol.hijo_izq == None) and(arbol.hijo_der == None)):
            return(None)
        elif((arbol.hijo_izq != None) and(arbol.hijo_der == None)):
            return(arbol.hijo_izq)
        elif((arbol.hijo_izq == None) and(arbol.hijo_der != None)):
            return(arbol.hijo_der)
        else:#dos hijos
            menor_de_mayores = buscaMinimo(arbol.hijo_der)
            arbol.dato = menor_de_mayores.dato
            arbol.hijo_der = eliminaValorAbb(arbol.hijo_der, arbol.dato)
    return(arbol)

def buscaMinimo(arbol: Abb | None) -> Abb:
    if(arbol == None):
        return(None)
    minimo = arbol
    siguiente = arbol.hijo_izq
    while(siguiente != None):
        minimo = siguiente
        siguiente = siguiente.hijo_izq
    return(minimo)

def recorreAbbEnOrden(arbol: Abb | None):
    if(arbol != None):
        recorreAbbEnOrden(arbol.hijo_izq)
        print(f"{arbol.dato}")
        recorreAbbEnOrden(arbol.hijo_der)

def eliminaAbb(arbol: Abb | None) -> Abb:
    if(arbol!=None):
        arbol.hijo_izq = None
        arbol.hijo_der = None
    return(None)

# Recorre recursivamente un arbol en orden y genera salida gv en archivo,
# retorna el numero de nodos visitados 
def recorreArbolGV(arbol: Abb, archivo: any) -> int:
    if(arbol == None):
        return(0)
    else:
        visitadosIzq = recorreArbolGV(arbol.hijo_izq, archivo)
        if(arbol.hijo_izq != None):
            archivo.write(f'{arbol.dato} -> {arbol.hijo_izq.dato} [label="hi"]\n')
        else:
            archivo.write(f'iNULL{arbol.dato} [shape=point];\n')
            archivo.write(f'{arbol.dato} -> iNULL{arbol.dato} [label="hi"]\n')
        if(arbol.hijo_der != None):
            archivo.write(f'{arbol.dato} -> {arbol.hijo_der.dato} [label="hd"]\n')
        else:
            archivo.write(f'dNULL{arbol.dato} [shape=point];\n')
            archivo.write(f'{arbol.dato} -> dNULL{arbol.dato} [label="hd"]\n')
        visitadosDer = recorreArbolGV(arbol.hijo_der, archivo)
    return(visitadosIzq + 1 + visitadosDer)

# Crea archivo gv para arbol
def muestraArbolGV(arbol: Abb | None, prefijo: str, version: int) -> int:
    archivo = open(f'{prefijo}{version}.dot', 'w')
    archivo.write(f'digraph {prefijo}{version} \n {{\n')
    auxTamano = recorreArbolGV(arbol, archivo);
    archivo.write(f"}}\n")
    archivo.close()
    return(auxTamano)




