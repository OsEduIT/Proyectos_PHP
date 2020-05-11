# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:33:53 2020

@author: oscar
"""


def hi(nombre,edad,direccion):
    print("Hola",nombre,"usted tiene ",edad," años y vive en ", direccion)
def sustraccion(num1,num2):
    print(num1-num2)
def mensaje():
    print("Ingrese un valor: ")
def multiply(n1,n2):
 return n1*n2    
def deseos():
 print("Te deseo ")
 return ("Happy Birthday") 
deseos()   
print(deseos())
x = input("Ingrese su nombre: ")    
y = input("Ingrese su edad: ")
z = input("Ingrese su direccion: ")
hi(x,y,z)   
mensaje()
a = int(input())
b = int(input())
print("El resultado de la resta es: ")
sustraccion(a,b)
print("El resultado de la multiplicación es: ")
w = multiply(a, b)
print(w)
#print(multiply(a, b)) 