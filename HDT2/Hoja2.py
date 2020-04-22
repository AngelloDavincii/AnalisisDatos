'''
Angel David Cuellar
18382
Hoja de trabajo 2
Metodo de biseccion
'''


from numpy import exp
import pandas as pd
from tabulate import tabulate



def bisec (funcion, a, b, error = 0.05):
    xl, xr, xu = a, b, b #designamos valores a variables
    ea = 100 #Designamos valor inicial al valor
    datos = {"I":[],"XL": [],"XR": [], "XU": [], "E": [] }
    contador = 0
    while ea > error:
        xrold = xr #creamos variable para hacer calculo de error
        xr = (xl + xu)/2 #calculo de xr
        if (f(xl) * f(xr) < 0): #condicionales para criterio del metodo
            xu = xr #cambiamos valores

        elif (f(xr) * f(xu)<0):
            xl = xr

        else:
            return xr

        ea = abs((xr-xrold)/xr)*100 #calculo de error

        contador = contador + 1
        datos["I"].append(contador)
        datos["XL"].append(xl)  #agregamos valores a listas y diccionario
        datos["XR"].append(xr)
        datos["XU"].append(xu)
        datos["E"].append(ea)
        
    return datos #retornamos diccionario


def falsaPosicion (funcion, a, b, error = 0.05):
    xl, xr, xu = a, b, b #designamos valores a variables
    ea = 100 #Designamos valor inicial al valor
    datos = {"I":[],"XL": [],"XR": [], "XU": [], "E": []}
    contador = 0
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
        contador = contador + 1
        datos["I"].append(contador) 
        datos["XL"].append(xl)  #agregamos valores a listas y diccionario
        datos["XR"].append(xr)
        datos["XU"].append(xu)
        datos["E"].append(ea)
  
     
    return datos #retornamos diccionario



#Metodo de impresion usando Data Frame de libreria pandas

def printDF (diccionario):
    print ("\n"*2)
    print ("              Imprimiendo con Data Frame")
    print ("")
    df= pd.DataFrame(diccionario)#usamos libreria pandas para usar data frame
    print (df)
    
  


#Metodo de impresion usando libreria Tabulate 

def printTabulate (diccionario, encabezado):
    print ("\n"*2)
    print ("                Imprimiendo con Tabulate")
    print ("")
    df= pd.DataFrame(diccionario)#usamos funcion de libreria de DataFrame
    print (tabulate(df, headers = encabezado, tablefmt = "grid"))#Usamos tabulate

def resultado (diccionario):
    result = diccionario["XR"][-1]
    print (result)

def resultIte (diccionario):
    result = diccionario["XR"][-1]
    ite = diccionario["I"][-1]
    print("")
    print ("La raiz de la funcion es ", result, " y el numero de iteraciones es ", ite)
#############################


def f(x):
    return exp(-x) - x

re = bisec (f, 0, 1)
printDF(re)
headers = ["XL", "XR", "XU", "E"]
printTabulate (re, headers)


def menu():
    print ("")
    print("        Bienvenido a este programa")
    print("1. Metodo de Biseccion")
    print("2. Metodo de falsaPosicion")
    print("3. Salir")
    print ("")
    method = input("Ingresa el numero correspondiente para usar metodo: ")
    
    while method != 3:
        if method == "1":
            print ("")
            print("1. Desplegar solucion")
            print("2. Desplegar solucion con numero de iteraciones")
            print("3. Imprimir todas las iteraciones tabuladas")
            print ("")
            work = input("Ingresa el numero de lo que deseas hacer: ")
            
            if work == "1":
                re = bisec (f, 0, 1)
                print("")
                print("La raiz de esta funcion es: ")
                resultado(re)
            if work == "2":
                re = bisec (f, 0, 1)
                resultIte(re)
            if work == "3":
                re = bisec (f, 0, 1)
                printDF(re)
                headers = ["Iteraciones","XL", "XR", "XU", "E"]
                printTabulate (re, headers)

                
        if method == "2":
            print ("")
            print("1. Desplegar solucion")
            print("2. Desplegar solucion con numero de iteraciones")
            print("3. Imprimir todas las iteraciones tabuladas")
            print ("")
            work = input("Ingresa el numero de lo que deseas hacer: ")
            
            if work == "1":
                dat = falsaPosicion (f, 0, 1)
                print("")
                print("La raiz de esta funcion es: ")
                resultado(dat)
            if work == "2":
                dat = falsaPosicion (f, 0, 1)
                resultIte(dat)
            if work == "3":
                dat = falsaPosicion (f, 0, 1)
                printDF(dat)
                headers = ["Iteraciones","XL", "XR", "XU", "E"]
                printTabulate (dat, headers)
            
        print ("")
        print("1. Metodo de Biseccion")
        print("2. Metodo de falsaPosicion")
        print("3. Salir")
        method = input("Ingresa el numero correspondiente para usar metodo: ")
        print ("")
        
    print ("Hasta luego")

menu()
