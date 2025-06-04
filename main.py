from abb import *

unArbol = None
unArbol = insertaValorAbb(unArbol, 50)
unArbol = insertaValorAbb(unArbol, 25)
unArbol = insertaValorAbb(unArbol, 12)
unArbol = insertaValorAbb(unArbol, 40)
unArbol = insertaValorAbb(unArbol, 30)
unArbol = insertaValorAbb(unArbol, 5)
unArbol = insertaValorAbb(unArbol, 75)
unArbol = insertaValorAbb(unArbol, 70)
unArbol = insertaValorAbb(unArbol, 80)
unArbol = insertaValorAbb(unArbol, 95)
tamano = muestraArbolGV(unArbol, "abb", 1)
print(f"GV> Nodos visitados: {tamano}")
recorreAbbEnOrden(unArbol);
unArbol = eliminaValorAbb(unArbol, 75);
tamano = muestraArbolGV(unArbol, "abb", 2);
print(f"GV> Nodos visitados: {tamano}")
recorreAbbEnOrden(unArbol);
