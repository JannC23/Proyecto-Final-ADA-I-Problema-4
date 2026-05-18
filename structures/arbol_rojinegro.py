from nodo_rango import Nodo

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, nodo):
        if self.raiz is None:
            self.raiz = nodo
            nodo.color = 'negro'
        else:
            actual = self.raiz
            padre = None
            while actual is not None:
                padre = actual
                if nodo.inicio < actual.inicio:
                    actual = actual.left
                elif nodo.inicio == actual.inicio:
                    actual = actual.left
                else:
                    actual = actual.right
                
            
            
            
    def corregir_insercion():