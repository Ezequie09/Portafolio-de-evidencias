class Coche:
    def __init__(self, marca, velocidad_maxima):
        self.__marca = marca  # Atributo privado
        self.__velocidad_maxima = velocidad_maxima  # Atributo privado
        self.__velocidad_actual = 0  # Atributo privado

    # Método público para acelerar, con una restricción
    def acelerar(self, incremento):
        if self.__velocidad_actual + incremento > self.__velocidad_maxima:
            self.__velocidad_actual = self.__velocidad_maxima
            print("Has alcanzado la velocidad máxima.")
        else:
            self.__velocidad_actual += incremento

    # Método público para obtener la velocidad actual
    def obtener_velocidad(self):
        return self.__velocidad_actual

# Uso de la clase
mi_coche = Coche("Toyota", 180)

mi_coche.acelerar(50)
print("Velocidad actual:", mi_coche.obtener_velocidad())  # 50
mi_coche.acelerar(150)
print("Velocidad actual:", mi_coche.obtener_velocidad())  # 180 (máxima velocidad)

# Intentando acceder a un atributo privado directamente causará un error
# print(mi_coche.__velocidad_actual)  # Descomentar esto causará un error