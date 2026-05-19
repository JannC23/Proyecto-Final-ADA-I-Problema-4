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
                    return
                else:
                    actual = actual.right
            nodo.padre = padre
            if nodo.inicio < padre.inicio:
                padre.left = nodo
            else:
                padre.right = nodo
            self._corregir_insercion(nodo)

    def _corregir_insercion(self, nodo):
        while nodo != self.raiz and nodo.padre.color == 'rojo':
            if nodo.padre == nodo.padre.padre.left:
                tio = nodo.padre.padre.right
                if tio.color == 'rojo':
                    tio.color = 'negro'
                    nodo.padre.padre.color = 'rojo'
                    nodo.padre.color = 'negro'
                    nodo = nodo.padre.padre
                else:
                    if nodo.padre.right == nodo :
                        self._rotar_izquierda(nodo.padre)
                        nodo = nodo.padre
                        aux = nodo.padre.color
                        nodo.padre.color = nodo.color
                        nodo.color = aux
                        self._rotar_derecha(nodo.padre) 
                    else:
                        aux = nodo.padre.padre.color
                        nodo.padre.padre.color = nodo.padre.color
                        nodo.padre.color = aux
                        self._rotar_derecha(nodo.padre.padre)
                        nodo = nodo.padre
            else:
                tio = nodo.padre.padre.left
                if tio.color == 'rojo':
                    tio.color = 'negro'
                    nodo.padre.padre.color = 'rojo'
                    nodo.padre.color = 'negro'
                    nodo = nodo.padre.padre
                else:
                    if nodo.padre.left == nodo :
                        self._rotar_derecha(nodo.padre)
                        nodo = nodo.padre
                        aux = nodo.padre.color
                        nodo.padre.color = nodo.color
                        nodo.color = aux
                        self._rotar_izquierda(nodo.padre)
                    else:
                        aux = nodo.padre.padre.color
                        nodo.padre.padre.color = nodo.padre.color
                        nodo.padre.color = aux
                        self._rotar_izquierda(nodo.padre.padre)
                        nodo = nodo.padre
        self.raiz.color = 'negro'
                
    def _rotar_izquierda(self, nodo):
          