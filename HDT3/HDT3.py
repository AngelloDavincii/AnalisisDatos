'''
Angel David Cuellar
18382
Hoja de trabajo 3
Newton rapson y punto fijo
'''

##Trate de sacar derivadas con funciones pero no lo logre

import pandas as pd
from tabulate import tabulate
import sympy as sym
from numpy import exp



def f(x):
    return exp(-x) - x

def prime(x):
    return -exp(-x) - 1

def g(x):
    return exp(-x)

def Rapson (funcion, derivada, a ,error = 0.05):
    xo = a #designamos valores a variables
    ea = 100 #Designamos valor inicial al error aproximamdo
    
    datos = {"I":[],"Xo":[], "E": [] }
    contador = 0
    while ea > error:
        xrold = xo #se guarda valor de iteracion  anterior
        
        xo = xo - (f(xo)/prime(xo))#se vuelve a calcular el xo
  

        ea = abs((xo-xrold)/xo)*100 #calculo de error

        contador = contador + 1
        datos["I"].append(contador)
        datos["Xo"].append(xo)  #agregamos valores a listas y diccionario
        datos["E"].append(ea)
        
    return datos #retornamos diccionario


def puntoFijo (funcion, a):
    error = 0.001 #si el error es muy alto la precision es mala
    xr= a #designamos valores a variables

    datos = {"I":[],"Xo": [], "E": []}
    y = 0
    contador = 0
    while y == 0 :
        xrold = xr #creamos variable para hacer calculo de error

        xr = g(xr)#evaluamos xr en la funcion despejada para x

        if (abs(g(xr)-g(xrold))<= error):#miramos que la evaluada de las dos
            y = 1 #derivadas sean menores al error
            
        contador = contador + 1

        datos["I"].append(contador) 
        datos["Xo"].append(xr)
        datos["E"].append(xr - xrold)
  
    print(datos)
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
    result = diccionario["Xo"][-1]
    print (result)

def resultIte (diccionario):
    result = diccionario["Xo"][-1]
    ite = diccionario["I"][-1]
    print("")
    print ("La raiz de la funcion es ", result, " y el numero de iteraciones es ", ite)
#############################




def menu():
    print ("")
    print("        Bienvenido a este programa")
    print("1. Metodo de Newton-Rapsom")
    print("2. Metodo del punto fijo")
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
            
            if work == 1:
                re = Rapson (f, prime, 1)
                print("")
                print("La raiz de esta funcion es: ")
                resultado(re)
            if work == "2":
                re = Rapson (f, prime, 1)
                resultIte(re)
            if work == "3":
                re = Rapson (f, prime, 1)
                printDF(re)
                headers = ["Iteraciones","Xo", "E"]
                printTabulate (re, headers)

                
        if method == 2:
            print ("")
            print("1. Desplegar solucion")
            print("2. Desplegar solucion con numero de iteraciones")
            print("3. Imprimir todas las iteraciones tabuladas")
            print ("")
            work = input("Ingresa el numero de lo que deseas hacer: ")
            
            if work == "1":
                dat = puntoFijo (g, 1)
                print("")
                print("La raiz de esta funcion es: ")
                resultado(dat)
            if work == "2":
                dat = puntoFijo (g, 1)
                resultIte(dat)
            if work == "3":
                dat = puntoFijo (g, 1)
                printDF(dat)
                headers = ["Iteraciones","Xo", "E"]
                printTabulate (dat, headers)
            
        print ("")
        print("1. Metodo de Newton-Rapsom")
        print("2. Metodo del punto fijo")
        print("3. Salir")
        method = int(input("Ingresa el numero correspondiente para usar metodo: "))
        print ("")
        
    print ("Hasta luego")

menu()

