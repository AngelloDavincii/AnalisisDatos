"""
Angel David Cuellar Bautista
Carnet 18382
Hoja De Trabajo 4
"""
#TOMAR EN CUENTA QUE EL TRABAJO FUE REALIZADO EN PYTHON 3.8.2
#No se porque no pude utilizar la libreria pylab
from numpy import *
from numpy import linalg as LA
import sympy as sp
from gekko import GEKKO

#Basado en el elaborado en clase
def inciso1(a , b, error):
    n=len(a)#largo del vector
    xe=zeros(n)#raices del vector
    res=b-dot(a,xe)#producto punto
    cont = 0
    while(LA.norm(res)>error):#se calcula error
        xe=array([(b[k]-dot(a[k,arange(n)!=k], xe[arange(n)!=k]))/a[k,k] for k in arange(n)])  
        res=b-dot(a,xe)#se vuelve a hacer producto punto
        cont=cont+1
    return(xe,cont)


def f(z,y):
    return (4-y-2*z)/4

def g(x,z):
    return (7 - 3*x - z)/5

def h(x,y):
    return (3 - x - y)/3
"""
def f1(w,y,z):
    return sp.real_root(5-3*y**2+z**3-w**2,2)

def g1(w,x,z):
    return sp.real_root((-x**3 + 10*z - w)/2,2)

def h1(w,x,y):
    return sp.real_root(-x**2-y**3+w-20,2)

def r(x,y,z):
    return sp.real_root(10-x+y**3-z,3)
"""
x,y,z,w = sp.symbols("x y z w")
CG1,CG2,CG3,CG4,CG5,CL1,CL2,CL3,CL4,CL5 = sp.symbols("CG1 CG2 CG3 CG4 CG5 CL1 CL2 CL3 CL4 CL5")
def gauss(error):
    
    ea = 100
    cont = 0
    a,b,c = 0,0,0
    while ea > error:
        aold = c
        #se evalua en las funciones con el f(x+1)
        a = (f(c,b))
        b = g(c,a)
        c = h(b,a)
        #se calcula el error
        ea = abs((c - aold)/c)*100
        cont = cont + 1#iteraciones
        
    return (a,b,c,cont)
#MIRA
#Deberas intente hacer el inciso 2 por gauss seidel como dijo Aristondo
#Y tambien con geeko pero al parecer no existe solucion para este problema
#OJO tambien ingrese el problema en Wolfram y no me lo caca

def inciso2(remote = False):
    #se intento con esta libreria que se usa para resolver ecuaciones de este tipo
    a = GEKKO()
    x = a.Var(value = 1)
    y = a.Var(value = 1)
    w = a.Var(value = 1)
    z = a.Var(value = 1)
    a.Equation(x**2  + 3*y**2 - z**3 +w**2 - 5 == 0 )
    a.Equation(x**3 - 2*y**2 - 10*z + w == 0 )
    a.Equation(x**2 + y**3 + z**2 - w + 20 == 0 )
    a.Equation(x - y**3 + z + w**3 - 10 == 0)
    a.solve(disp = False)
    print(x.value,y.value,w.value,z.value)
"""
def gauss2(error):
    ea = 100
    cont = 0
    a,b,c,d = 0,0,0,0
    while ea > error:
        aold = d

        a = f1(a,c,d)
        b = g1(a,b,d)
        c = h1(a,b,c)
        d = r(b,c,d)

        ea = abs((d - aold)/d)*100
        cont = cont + 1
        
    return (a,b,c,d,cont)
"""
def menu():
    print ("")
    print("        Bienvenido a este programa")
    print("")
    print("1. Inciso 1")
    print("2. Inciso 2")
    print("3. Inciso 3")
    print("4. Inciso 4")
    print("5. Salir")
    print ("")
    method = int(input("Escriba el numero del inciso que va a calificar: "))
    
    while method != 5:
        if method == 1:
            matriz = array([[4,1,2],[3,5,1],[1,1,3]])
            respuesta = array([4,7,3])

            sol = inciso1(matriz, respuesta, 0.09)
            sol2 = gauss(0.09)
            
            print("--------------------METODO DE JACOBI-------------------------")
            print("Las soluciones al sistema de ecuaciones son:")
            print("x: ",round(sol[0][0],1)," y: ",round(sol[0][1],1)," z: ",round(sol[0][2],1))
            print("El numero de iteraciones para resolver el problema fueron: ")
            print(sol[1])
            print("\n"*2)
            print("--------------------  GAUSS SEIDEL   -------------------------")
            print("Las soluciones al sistema de ecuaciones son:")
            print("x: ",round(sol2[0],1)," y: ",round(sol2[1],1)," z: ",round(sol2[2],1))
            print("El numero de iteraciones para resolver el problema fueron: ")
            print(sol2[3])
            print("\n"*2)
            
        if method == 2:
            try:
                inciso2()
            except:
                print("No existe solucion a este problema")

        if method == 3:
            #escribimos las ecuaciones
            ec1 = sp.Eq(15*x + 17*y + 19*z - 3890, 0)
            ec2 = sp.Eq(0.3*x + 0.4*y + 0.55*z - 95, 0)
            ec3 = sp.Eq(x+ 1.2*y + 1.5*z - 282, 0)
            #metodo de sympy
            sol2 = sp.solve([ec1,ec2,ec3])
            print("")
            print("Las concentraciones para este problema son: ")
            print(sol2)
            print("")
 

        if method == 4:
            #variables dadas
            g = 2
            q = 1
            d = 0.8
            CG0 = 100
            CL6 = 10
            #lo mismo que el anterior
            ec1 = sp.Eq(g*(CG0 - CG1) + d*(CL1 - CG1),0)
            ec2 = sp.Eq(q*(CL2 - CL1) + d*(CG1 - CL1),0)
            ec3 = sp.Eq(g*(CG1 - CG2) + d*(CL2 - CG2),0)
            ec4 = sp.Eq(q*(CL3 - CL2) + d*(CG2 - CL2),0)
            ec5 = sp.Eq(g*(CG3 - CG3) + d*(CL3 - CG3),0)
            ec6 = sp.Eq(q*(CL4 - CL3) + d*(CG3 - CL3),0)
            ec7 = sp.Eq(g*(CG3 - CG4) + d*(CL4 - CG4),0)
            ec8 = sp.Eq(q*(CL5 - CL4) + d*(CG4 - CL4),0)
            ec9 = sp.Eq(g*(CG4 - CG5) + d*(CL5 - CG5),0)
            ec10 = sp.Eq(q*(CL6 - CL5) + d*(CG5 - CL5),0)

            sol2 = sp.solve([ec1,ec2,ec3,ec4,ec5,ec6,ec7,ec8,ec9,ec10])
            print("")
            print("El numero de componententes que se pueden producir al dia son: ")
            print(sol2)
            print("")
            
        print ("")
        print("        Bienvenido a este programa")
        print("")
        print("1. Inciso 1")
        print("2. Inciso 2")
        print("3. Inciso 3")
        print("4. Inciso 4")
        print("5. Salir")
        print ("")
        method = int(input("Escriba el numero del inciso que va a calificar: "))
        
    print ("Hasta luego")

menu()
