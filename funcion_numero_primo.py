# -*- coding: utf-8 -*-
"""
Created on Mon May 11 21:11:31 2020

@author: oscar
"""
#Números primos

def isPrime(num):
    if num < 2:     
     return False
    for i in range(2, num):  
      if num % i == 0:    
       return False
    return True    
k=True
while k==True:
 n = int(input("ingrese un número: "))
 n1 = input("Presione e para salir o enter para continuar  ")
 x = isPrime(n)    
 lista=[]
 if x==True:
    print("El número ",n, "es Primo." )
    print ("Sus primos anteriores son: ")
    for i in range(2,n):
        if n % i != 0:
            y = isPrime(i)
            if y == True:
               lista.append(i)
    print(lista)
 else:
    print("El número ",n, " no es Primo.")
    print ("Sus primos anteriores son: ")
    for i in range(1,n):
        if n % i != 0:
            y = isPrime(i)
            if y == True:
               lista.append(i)
    print(lista)
 if n1 == 'e':
     print("Gracias")
     break
 else:
     continue
 
 
 
  
