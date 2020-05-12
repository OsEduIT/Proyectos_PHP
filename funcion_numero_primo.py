# -*- coding: utf-8 -*-
"""
Created on Mon May 11 21:11:31 2020

@author: oscar
"""
#Números primos

def isPrime(num):
    if num < 2:     #si es menos que 2 no es primo, por lo tanto devolverá Falso
     return False
    for i in range(2, num):  #un rango desde el dos hasta el numero que nosotros elijamos
      if num % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
       return False
    return True    #de lo contrario devuelve Verdadero
k=True
while k==True:
 n = int(input("ingrese un número: "))
 n1 = input("Presione e para salir o enter para continuar  ")
 x = isPrime(n)    #para probarlo llamamos a la función
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
 
 
 
  