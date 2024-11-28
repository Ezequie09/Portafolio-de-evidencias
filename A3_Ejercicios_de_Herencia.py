import math
class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre= nombre
    def calcular_area(self):
        pass  

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio
    def calcular_area(self):
        return math.pi * self.radio ** 2

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return (self.base * self.altura) / 2
circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)
triangulo = Triangulo(3, 7)
print(f"Área del {circulo.nombre}: {circulo.calcular_area():.2f}") 
print(f"Área del {rectangulo.nombre}: {rectangulo.calcular_area():.2f}")  
print(f"Área del {triangulo.nombre}: {triangulo.calcular_area():.2f}")  
