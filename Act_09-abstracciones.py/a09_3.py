from abc import ABC, abstractmethod
# Interfaz
class IPaleta(ABC):
    @abstractmethod
    def mostrarInformacion(self):
        pass

    @abstractmethod
    def cambiarPrecio(self, incremento: float):
        pass

    @abstractmethod
    def agregarSaborExtra(self, sabor_extra: str):
        pass

# Clase Abstracta
class Paleta(IPaleta):
    def __init__(self, sabor: str, precio: float):
        self.sabor = sabor
        self.precio = precio
    def mostrarInformacion(self):
        print(f"Sabor: {self.sabor}, Precio: ${self.precio:.2f}")
    @abstractmethod
    def cambiarPrecio(self, incremento: float):
        pass
    @abstractmethod
    def agregarSaborExtra(self, sabor_extra: str):
        pass

class PaletaAgua(Paleta):
    def __init__(self, sabor: str, precio: float, baseAgua: bool):
        super().__init__(sabor, precio)
        self.baseAgua = baseAgua
    def mostrarBaseAgua(self):
        print(f"Base de Agua: {'Sí' if self.baseAgua else 'No'}")
    def cambiarPrecio(self, incremento: float = 2):
        super().cambiarPrecio(incremento)
    def derretirse(self):
        print(f"La paleta de {self.sabor} se está derritiendo rápidamente.")
    def agregarSaborExtra(self, sabor_extra: str):
        self.sabor += f" con un toque de {sabor_extra}"
        print(f"Ahora la paleta es de {self.sabor}.")

class PaletaCrema(Paleta):
    def __init__(self, sabor: str, precio: float, cremosa: bool):
        super().__init__(sabor, precio)
        self.cremosa = cremosa
    def mostrarTexturaCremosa(self):
        print(f"Textura Cremosa: {'Sí' if self.cremosa else 'No'}")
    def cambiarPrecio(self, incremento: float = 6):
        super().cambiarPrecio(incremento)
    def describirCremosidad(self):
        print(f"La paleta de {self.sabor} tiene una textura extremadamente cremosa." if self.cremosa else 
              f"La paleta de {self.sabor} no es tan cremosa.")
    def aplicarPromocion(self, descuento: float):
        if self.precio - descuento >= 0:
            self.precio -= descuento
            print(f"Promoción aplicada. El nuevo precio de la paleta de {self.sabor} es ${self.precio:.2f}")
        else:
            print("El descuento no puede dejar el precio negativo.")

# Ejemplo de uso
paleta_agua_fresa = PaletaAgua("Fresa", 15.0, True)
paleta_crema_chocolate = PaletaCrema("Chocolate", 20.0, True)
print("-"*100)
paleta_agua_fresa.mostrarInformacion() 
paleta_agua_fresa.mostrarBaseAgua()
paleta_agua_fresa.cambiarPrecio()
paleta_agua_fresa.mostrarInformacion()  
paleta_agua_fresa.derretirse()
paleta_agua_fresa.agregarSaborExtra("Limón")  
print("-"*100)
paleta_crema_chocolate.mostrarInformacion()  
paleta_crema_chocolate.mostrarTexturaCremosa() 
paleta_crema_chocolate.cambiarPrecio()
paleta_crema_chocolate.mostrarInformacion()
paleta_crema_chocolate.describirCremosidad() 
paleta_crema_chocolate.aplicarPromocion(5)
