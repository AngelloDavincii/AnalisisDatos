"""
Angel David Cuellar 18382
Hoja de Trabajo 1
ejercicio 2
"""

def euclides(a, b):
    resultado = 0
    if a < b:
        c = b - a
        
        while c !=0:
            b = a
            a = c
            c = b - a
            resultado = a
            
    elif a >= b:
        c = a - b

        while c !=0:
            a = b
            b = c
            c = a - b
            resultado = b

    print "Tu MCD es ", resultado
    print ("Gracias por usar este programa")
    print ("")

print ("Bienvenido a la calculadora de MCD")
print ("")
            

euclides (12,6)
euclides (15,9)
euclides (9,15)
euclides (10,8)


