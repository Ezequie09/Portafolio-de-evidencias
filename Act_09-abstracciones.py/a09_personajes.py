from abc import ABC, abstractmethod
class Personaje(ABC):
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel 
    @abstractmethod
    def atacar(self):
        pass

class HabilidadesMagicas(ABC):
    @abstractmethod
    def lanzarHechizo(self):
        pass

class HabilidadesFisicas(ABC):
    @abstractmethod
    def usarHabilidadFisica(self):
        pass

class Jugador(Personaje, HabilidadesFisicas):
    def __init__(self, nombre, nivel, clase):
        super().__init__(nombre, nivel)
        self.clase = clase
    def atacar(self):
        print(f"{self.nombre}: ¡ATAQUEEEEN!")
    def usarHabilidadFisica(self):
        print(f"{self.nombre}, el {self.clase}, usa su habilidad física.")

class Enemigo(Personaje, HabilidadesMagicas):
    def __init__(self, nombre, nivel, tipo):
        super().__init__(nombre, nivel)
        self.tipo = tipo
    def atacar(self):
        print(f"{self.nombre}, el {self.tipo}, ¡ATAQUEEEEN!")
    def lanzarHechizo(self):
        print(f"{self.nombre}, el {self.tipo}, lanza un hechizo malvado.")

class HechiceroGuerrero(Personaje, HabilidadesMagicas, HabilidadesFisicas):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
    def atacar(self):
        print(f"{self.nombre}: ¡ATAQUEEEEN con magia y fuerza!")
    def lanzarHechizo(self):
        print(f"{self.nombre} lanza un poderoso hechizo.")
    def usarHabilidadFisica(self):
        print(f"{self.nombre} usa su fuerza física en combate.")

jugador = Jugador("Ezequiel", 10, "Guerrero")
enemigo = Enemigo("Messi", 15, "Orco Mago")
hechicero_guerrero = HechiceroGuerrero("Andromeda", 20)

print("-"*120)
jugador.atacar()
jugador.usarHabilidadFisica()
print()
enemigo.atacar()
enemigo.lanzarHechizo()
print()
hechicero_guerrero.atacar()
hechicero_guerrero.usarHabilidadFisica()
hechicero_guerrero.lanzarHechizo()
