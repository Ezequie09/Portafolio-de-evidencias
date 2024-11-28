import math

class MiExcepcion(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

def calcular_raiz_cuadrada(valor):
    try:
        if valor < 0:
           
            raise MiExcepcion("Error: No se puede calcular la raíz cuadrada de un número negativo.")
        return math.sqrt(valor)
    except MiExcepcion as e:
        
        print(e)

print(calcular_raiz_cuadrada(9))  
calcular_raiz_cuadrada(-4)         
