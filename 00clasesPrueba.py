import os
os.system('cls' if os.name == 'nt' else 'clear')

#importar clases
from ClasesEspeciales import Libro

libro1 = Libro("Stephen King", "It", 1032)
print(len(libro1))