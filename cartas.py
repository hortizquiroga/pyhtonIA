class Carta:
    def __init__(self, numero, mazo):
        self.mazo=mazo
        self.numero= numero
    def imprimir(self):
        print(self.numero, " de ", self.mazo)
carta1 = Carta(7, "Espadas")
carta1.imprimir()