class Persona:
    #Atributo clase
    especie = "humano"
    
    #Metodos de instancia

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
   #Metodo de instacia
        
    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre}')
        
    def cumplir_anios(self, estado_humor):
        print(f'Cumplir {self.edad + 1} años me pone {estado_humor}')
        
juan = Persona("Juan", 37)
juan.edad = 37

print(juan.edad)

