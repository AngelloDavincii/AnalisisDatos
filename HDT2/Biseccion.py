'''
Angel David Cuellar
18382
Hoja de trabajo 2
Metodo de biseccion
'''

import sympy as sp
from numpy import exp
import pandas as pd
from tabulate import tabulate
ALTURA = 4
VELOCIDAD = 10
x = sp.Symbol("x")
def f(vi , h, x):
    return -(1/-9.8)*vi**2*sp.cos(x)*sp.sin(x)-((vi*sp.cos(x))/-9.8)*((vi**2*sp.sin(x)**2)-2*-9.8*h)**(1/2)
    

def bisec (funcion, a, b, error = 0.000001):
    xl, xr, xu = a, b, b #designamos valores a variables
    ea = 100 #Designamos valor inicial al valor


    while ea > error:
        xrold = xr #creamos variable para hacer calculo de error
        xr = (xl + xu)/2 #calculo de xr
        if (f(VELOCIDAD,ALTURA,xl) * f(VELOCIDAD,ALTURA,xr) < 0): #condicionales para criterio del metodo
            xu = xr #cambiamos valores

        elif (f(VELOCIDAD,ALTURA,xl) * f(VELOCIDAD,ALTURA,xl)<0):
            xl = xr

        else:
            return xr

        ea = abs((xr-xrold)/xr)*100 #calculo de error

        print(ea)
    return xr #retornamos diccionario

re = bisec (f(VELOCIDAD,ALTURA,x), 0, 1.57)

print(re)


    
