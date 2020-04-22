"""
Angel David Cuellar 18382
Hoja de trabajo 1
Ejercicio 5
"""

def paquete(n):
    pack = []
    i = 0
    b = 1
    
    while i != len(n)-1:
        
        if n[i] == n[i+1]:
            b = b+1
            
        else:
            
            pack.append((n[i] , b))
        i = i + 1
        print (i)
        
            
    print(pack)


a = [1,1,1,3,5,1,1,3,3]
paquete (a)
