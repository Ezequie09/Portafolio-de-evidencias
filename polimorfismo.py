class Carro: 
    def encender(self): 
        pass 

class Deportivo(Carro): 
    def encender(self): 
        return "El deportivo ruge al encender" 

class SUV(Carro): 
    def encender(self): 
        return "El SUV enciende suavemente" 
    
class Electrico(Carro): 
    def encender(self): 
        return "El carro eléctrico enciende silenciosamente" 

carros = [Deportivo(), SUV(), Electrico()] 
for carro in carros: 
    print(carro.encender()) 

 