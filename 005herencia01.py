class Personaje:
    def __init__(self, nombre, herramienta):
        self.nombre = nombre
        self.arma = herramienta
        
class Mago(Personaje):
    pass

hechicero = Mago("Merlín","caldero")


import os
os.system('cls' if os.name == 'nt' else 'clear')

print(hechicero.nombre)
print(hechicero.arma)
