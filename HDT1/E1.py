"""
Angel David Cuellar 18382
Hoja de Trabajo 1
ejercicio 1
"""
import random

def adivinar(n):
    a = random.randrange(1,n+1)
    print(a)
    b=input("Por favor ingresa un numero entero: ")
    
    while a != b:
        b=input("Por favor ingresa un numero entero: ")

    print"Felicidades tu numera era " , a
    
    return n

adivinar(3)
