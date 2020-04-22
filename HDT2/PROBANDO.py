'''
Angel David Cuellar
18382
Hoja de trabajo 2
Metodo de Falsa Posicion
'''

import sympy as sp
from numpy import exp
import pandas as pd
from tabulate import tabulate
ALTURA = 4
VELOCIDAD = 10

def f(vi , h, x):
    return -(1/-9.8)*vi**2*sp.cos(x)*sp.sin(x)-((vi*sp.cos(x))/-9.8)*((vi**2*sp.sin(x)**2)-2*-9.8*h)**(1/2)
    

def puntoFijo (funcion, a, b, error = 0.0000001):
    xl, xr, xu = a, b, b #designamos valores a variables
    ea = 100 #Designamos valor inicial al valor


    while ea > error:
        xrold = xr #creamos variable para hacer calculo de error
        
        #ESTO ES LA UNICA DIFERENCIA CON EL DE BISECCION
        m = (f(VELOCIDAD,ALTURA,xu)-f(VELOCIDAD,ALTURA,xl))/(xu-xl)#calculamos m
        xr = xl - (f(VELOCIDAD,ALTURA,xl)/m)  #calculo de xr
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        
        if (f(VELOCIDAD,ALTURA,xl) * f(VELOCIDAD,ALTURA,xr) < 0): #condicionales para criterio del metodo
            xu = xr #cambiamos valores

        elif (f(VELOCIDAD,ALTURA,xr) * f(VELOCIDAD,ALTURA,xu)<0):
            xl = xr

        else:
            return xr

        ea = abs((xr-xrold)/xr)*100 #calculo de error

    return xr #retornamos diccionario

re = puntoFijo (f, 0, 1.57)
print (re)




