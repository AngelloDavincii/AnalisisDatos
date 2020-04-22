"""
Angel David Cuellar 18382
Hoja de Trabajo 1
ejercicio 3
"""

def amigos(n):
    divisores = []
    for i in range(1,n+1):
        if(n%i==0):
            divisores.append(i)
 
    divisores.pop()
    
    suma=0
    for m in divisores:
        suma=suma+m
        
    print "La suma de los divisores es: ", suma
    print ""
    return suma



print("Bienvenido al programa amigos")
print""
amigos(32)
