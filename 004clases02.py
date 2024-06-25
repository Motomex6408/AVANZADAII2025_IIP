class Aritmeticas:
    especie = "numeros"
    
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    #suma  
    def suma(self):
        print("La suma de", (self.n1), "y", (self.n2), "es", (self.n1 + self.n2))
        
    
    #resta    
    def resta(self):
        print("La resta de", (self.n1),  "y",  (self.n2), "es", (self.n1 -  self.n1))
        
    #multiplicacion
    def multiplicacion(self):
        print("La multiplicacion de", (self.n1), "y", (self.n2), "es", (self.n1 * self.n2))
    
    #division
    def division(self):
        print("La division de", (self.n1), "y", (self.n2), "es", (self.n1 / self.n2))

    #potencia
    def potencia(self):
        print("La potencia de", (self.n1), "y", (self.n2),  "es", (self.n1 ** self.n2))
        
import os
os.system('cls' if os.name == 'nt' else 'clear')

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))

aritmetica = Aritmeticas(n1, n2)  

aritmetica.suma()
aritmetica.resta()
aritmetica.multiplicacion()
aritmetica.division()
aritmetica.potencia()