from structures.arbol_rojinegro import Arbol
from structures.nodo_rango import Nodo


class MotorConsultas:

    def __init__(self):
        self.arbol = Arbol()

    def inorder(self, nodo, resultado):
        if nodo is not None:
            self.inorder(nodo.left, resultado)
            resultado.append(nodo)
            self.inorder(nodo.right, resultado)

    def obtener_rangos(self):
        resultado = []
        self.inorder(self.arbol.raiz, resultado)
        return resultado

    def agregar_rango(self, valor, inicio, fin):
        nodo = Nodo(inicio, fin, valor)
        self.arbol.insertar(nodo)

    def value(self, posicion):
        rangos = self.obtener_rangos()

        for nodo in rangos:
            if nodo.inicio <= posicion <= nodo.fin:
                return nodo.valor
        return None

    def suma(self, inicio, fin):
        total = 0
        rangos = self.obtener_rangos()

        for nodo in rangos:
            inter_inicio = max(inicio, nodo.inicio)
            inter_fin = min(fin, nodo.fin)
            
            if inter_inicio <= inter_fin:
                cantidad = inter_fin - inter_inicio + 1
                total += cantidad * nodo.valor
        return total

    def frequency(self, valor):
        total = 0
        rangos = self.obtener_rangos()
        
        for nodo in rangos:
            if nodo.valor == valor:
                total += (nodo.fin - nodo.inicio + 1)
        return total

    def max_range(self, inicio, fin):
        mayor = None
        rangos = self.obtener_rangos()

        for nodo in rangos:
            if nodo.fin < inicio or nodo.inicio > fin:
                continue
            if mayor is None or nodo.valor > mayor:
                mayor = nodo.valor
        return mayor

    def min_range(self, inicio, fin):
        menor = None
        rangos = self.obtener_rangos()

        for nodo in rangos:
            if nodo.fin < inicio or nodo.inicio > fin:
                continue
            if menor is None or nodo.valor < menor:
                menor = nodo.valor
        return menor

    def decompress(self, inicio, fin):
        resultado = []
        rangos = self.obtener_rangos()

        for nodo in rangos:
            inter_inicio = max(inicio, nodo.inicio)
            inter_fin = min(fin, nodo.fin)

            if inter_inicio <= inter_fin:
                cantidad = inter_fin - inter_inicio + 1

                for _ in range(cantidad):
                    resultado.append(str(nodo.valor))

        return " ".join(resultado)

    def count_ranges(self):
        return len(self.obtener_rangos())

    def merge(self):
        rangos = self.obtener_rangos()

        if len(rangos) == 0:
            return
        
        nuevos = []
        actual = rangos[0]

        for i in range(1, len(rangos)):
            siguiente = rangos[i]

            if actual.valor == siguiente.valor and actual.fin + 1 == siguiente.inicio:
                actual.fin = siguiente.fin
            else:
                nuevos.append(actual)
                actual = siguiente
                
        nuevos.append(actual)
        self.arbol = Arbol()

        for nodo in nuevos:
            self.agregar_rango(nodo.valor, nodo.inicio, nodo.fin)

    def update(self, inicio, fin, nuevo_valor):
        rangos = self.obtener_rangos()
        nuevos = []

        for nodo in rangos:
            if nodo.fin < inicio or nodo.inicio > fin:
                nuevos.append(nodo)
            else:
                if nodo.inicio < inicio:
                    izquierda = Nodo(
                        nodo.inicio,
                        inicio - 1,
                        nodo.valor
                    )
                    nuevos.append(izquierda)

                if nodo.fin > fin:
                    derecha = Nodo(
                        fin + 1,
                        nodo.fin,
                        nodo.valor
                    )
                    nuevos.append(derecha)

        nuevos.append(Nodo(inicio, fin, nuevo_valor))
        self.arbol = Arbol()

        for nodo in nuevos:
            self.agregar_rango(nodo.valor, nodo.inicio, nodo.fin)
        self.merge()