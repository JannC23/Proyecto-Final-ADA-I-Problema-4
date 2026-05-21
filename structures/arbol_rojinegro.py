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
        y = nodo.right      
        nodo.right = y.left
        y.padre = nodo.padre 
        if y.padre is None:
            self.raiz = y
        elif y.padre.left == nodo:
            y.padre.left = y
        elif y.padre.right == nodo:
            y.padre.right = y
        y.left = nodo
        nodo.padre = y  
        if nodo.right is not None:
            nodo.right.padre = nodo
        
    def _rotar_derecha(self, nodo):
        y = nodo.left
        nodo.left = y.right
        y.padre = nodo.padre 
        if y.padre is None:
            self.raiz = y
        elif y.padre.left == nodo:
            y.padre.left = y
        elif y.padre.right == nodo:
            y.padre.right = y
        y.right = nodo
        nodo.padre = y
        if nodo.left is not None:
            nodo.left.padre = nodo
    
    def buscar(self, inicio):
        def _buscar_aux(self, nodo, inicio):
            if nodo == None:
                return None
            elif nodo.inicio == inicio:
                return nodo
            else:
                if nodo.inicio < inicio:
                    return _buscar_aux(nodo.left, inicio)
                else: 
                    return _buscar_aux(nodo.right, inicio)
        return _buscar_aux(self.raiz, inicio)
        
    def transplantar(self, u, v):
        if u.padre == None:
            self.raiz = v
        elif u.padre.left == u:
            u.padre.left = v
        else:
            u.padre.right = v
        if v is not None:
            v.padre = u.padre
    
    def eliminar(self, inicio):
        nodo = self.buscar(inicio)
        if nodo is None:
            return
        
        y = nodo
        y_color_original = y.color
        
        if nodo.left is None:
            x = nodo.right
            self.transplantar(nodo, nodo.right)
        elif nodo.right is None:
            x = nodo.left
            self.transplantar(nodo, nodo.left)
        else:
            y = nodo.right
            while y.left is not None:
                y = y.left
            y_color_original = y.color
            x = y.right
            if y.padre == nodo:
                if x is not None:
                    x.padre = y
            else:
                self.transplantar(y, y.right)
                y.right = nodo.right
                y.right.padre = y
            self.transplantar(nodo, y)
            y.left = nodo.left
            y.left.padre = y
            y.color = nodo.color
        
        if y_color_original == 'negro' and x is not None:
            self._corregir_eliminacion(x)

    def _corregir_eliminacion(self, nodo):
        while nodo != self.raiz and nodo.color == 'negro':
            if nodo == nodo.padre.left:
                hermano = nodo.padre.right
                if hermano is not None and hermano.color == 'rojo':
                    hermano.color = 'negro'
                    nodo.padre.color = 'rojo'
                    self._rotar_izquierda(nodo.padre)
                    hermano = nodo.padre.right
                if (hermano is None or 
                    (hermano.left is None or hermano.left.color == 'negro') and
                    (hermano.right is None or hermano.right.color == 'negro')):
                    if hermano is not None:
                        hermano.color = 'rojo'
                    nodo = nodo.padre
                else:
                    if hermano is not None and (hermano.right is None or hermano.right.color == 'negro'):
                        if hermano.left is not None:
                            hermano.left.color = 'negro'
                        if hermano is not None:
                            hermano.color = 'rojo'
                        self._rotar_derecha(hermano)
                        hermano = nodo.padre.right
                    if hermano is not None:
                        hermano.color = nodo.padre.color
                    nodo.padre.color = 'negro'
                    if hermano is not None and hermano.right is not None:
                        hermano.right.color = 'negro'
                    self._rotar_izquierda(nodo.padre)
                    nodo = self.raiz
            else:
                hermano = nodo.padre.left
                if hermano is not None and hermano.color == 'rojo':
                    hermano.color = 'negro'
                    nodo.padre.color = 'rojo'
                    self._rotar_derecha(nodo.padre)
                    hermano = nodo.padre.left
                if (hermano is None or
                    (hermano.right is None or hermano.right.color == 'negro') and
                    (hermano.left is None or hermano.left.color == 'negro')):
                    if hermano is not None:
                        hermano.color = 'rojo'
                    nodo = nodo.padre
                else:
                    if hermano is not None and (hermano.left is None or hermano.left.color == 'negro'):
                        if hermano.right is not None:
                            hermano.right.color = 'negro'
                        if hermano is not None:
                            hermano.color = 'rojo'
                        self._rotar_izquierda(hermano)
                        hermano = nodo.padre.left
                    if hermano is not None:
                        hermano.color = nodo.padre.color
                    nodo.padre.color = 'negro'
                    if hermano is not None and hermano.left is not None:
                        hermano.left.color = 'negro'
                    self._rotar_derecha(nodo.padre)
                    nodo = self.raiz
        nodo.color = 'negro'