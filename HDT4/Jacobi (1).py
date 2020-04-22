## Método de Jacobi
## Resolver el sistema de ecuaciones:
## 4x+y+2z=4
## 3x+5y+z=7
## x+y+3z=3
#from numpy import array, zeros, dot
from numpy import array, dot, arange, zeros, linalg as LA

A = array([[4,1,2],[3,5,1],[1,1,3]])

b= array([4,7,3])

def jacobi(a,b,error):
    n=len(a)
    x=zeros(n)
    res=b-dot(a,x)
    cont = 0
    while(LA.norm(res)>error):
        x=array([(b[k]-dot(a[k,arange(n)!=k], x[arange(n)!=k]))/a[k,k] for k in arange(n)])    #x es el vector solución
        res=b-dot(a,x)
        cont=cont+1
    return(x,cont)
print(jacobi(A,b,0.05))
