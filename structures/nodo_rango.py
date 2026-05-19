class Nodo:
    def __init__(self, inicio, fin, valor):
        self.valor = valor
        self.left = None
        self.right = None
        self.inicio = inicio
        self.fin = fin
        self.color = 'rojo'
        self.padre = None
