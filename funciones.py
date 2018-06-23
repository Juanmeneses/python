from math import *

def f(x):
    y = 2*x**2+1
    return y

def areatriangulo(a,b,c):
    area = a+b+c
    return area

def cuadrado(L):
    cuad = L**2
    return cuad

def rectangulo (a,b):
    area = a*b
    return area

def circulo(h):
    area = pi * h ** 2
    return area

def diferencia(num1, num2):
    if(num1>num2):
        aux = num1
        num1 = num2
        num2 = aux
    for i in range (num1+1, num2):
        print(i)

diferencia(15,10)
b=4
c=3
for x in range(5):
    y= areatriangulo(x,b,c)
    q = cuadrado(x)
    w = rectangulo(x,b)
    e = circulo(x)
    print(f"funcion 1 = {x}, Funcion 2 = {y}, Funcion 3 = {q}, Funcion 4 = {w}, Función PI {e}")



