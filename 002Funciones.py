# Crea una función llamada devolver_distintos() que reciba 3
# integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el
# número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el
# número menor.
# Si la suma de los 3 números es un valor entre 10 y 15
# (incluidos) va a devolver el número de valor intermedio

import os
os.system('cls' if os.name == 'nt' else 'clear')

def devolver_distintos(n1,n2,n3):
    suma= n1+n2+n3
    if suma > 15:
        print(max(n1,n2,n3))
    elif suma < 10:
        print(min(n1,n2,n3))
    else:
        suma= n1+n2+n3 - max(n1,n2,n3) - min(n1,n2,n3)
    return suma
        
print(devolver_distintos(2,5,10))

def ordenar(n1,n2,n3):
    print(sorted([n1,n2,n3]))
    
print(ordenar(19,5,10))