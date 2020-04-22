'''
Angel David Cuellar
18382
Hoja de trabajo
Ejercicio 5
'''

def paquete(n):
    paquete = []
        
    for i in n:
        b=1
        if i == n[i+1]:
            paquete.append((i,b))
            b = b+1
            
        else:
            paquete.append((i,b))
    print (paquete)   

a = [1,1,1,3,5,1,1,3,3]
paquete(a)
