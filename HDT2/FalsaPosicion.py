'''
Angel David Cuellar
18382
Hoja de trabajo 2
Metodo de Falsa Posicion
'''


from numpy import exp
import pandas as pd
from tabulate import tabulate

def f(x):
    return exp(-x) - x

def bisec (funcion, a, b, error = 0.05):
    xl, xr, xu = a, b, b #designamos valores a variables
    ea = 100 #Designamos valor inicial al valor
    datos = {"XL": [],"XR": [], "XU": [], "E": []}

    while ea > error:
        xrold = xr #creamos variable para hacer calculo de error
        
        #ESTO ES LA UNICA DIFERENCIA CON EL DE BISECCION
        m = (f(xu)-f(xl))/(xu-xl)#calculamos m
        xr = xl - (f(xl)/m)  #calculo de xr
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        
        if (f(xl) * f(xr) < 0): #condicionales para criterio del metodo
            xu = xr #cambiamos valores

        elif (f(xr) * f(xu)<0):
            xl = xr

        else:
            return xr

        ea = abs((xr-xrold)/xr)*100 #calculo de error
        datos["XL"].append(xl)  #agregamos valores a listas y diccionario
        datos["XR"].append(xr)
        datos["XU"].append(xu)
        datos["E"].append(ea)
        
    return datos #retornamos diccionario

re = bisec (f, 0, 1)
#Metodo de impresion usando Data Frame de libreria pandas
def printDF (diccionario):
    df= pd.DataFrame(diccionario)#usamos libreria pandas para usar data frame
    print (df)
    
  

printDF(re)

print ("\n"*4)
headers = ["XL", "XR", "XU", "E"]
#Metodo de impresion usando libreria Tabulate 

def printTabulate (diccionario, encabezado):
    df= pd.DataFrame(diccionario)#usamos funcion de libreria de DataFrame
    print (tabulate(df, headers = encabezado, tablefmt = "grid"))#Usamos tabulate


printTabulate (re, headers)
    






