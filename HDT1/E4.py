"""
Angel David Cuellar 18382
Hoja de Trabajo 1
ejercicio 4
"""

def multiplos (a , b):
    divisores = []
    for i in range(1,a+1):
        if(a%i==0):
            divisores.append(i)

    final = []
    for s in divisores:
        if (s < b):
            final.append(s)

    print final

multiplos (50,30)
        
    
