# -*- coding: utf-8 -*-
"""
Created on Mon May 11 19:00:59 2020

@author: oscar
"""

def l100kmtompg():
    l = float(input("Ingrese los litros: "))    
    print("Se consume ",l,"lts/Km en Europa")
    aux = l*(1609.344)
    aux2 = 1000*(3.785411784)
    conv = (aux2/aux)*100 
    return conv
def mpgtol100km():
     m = float(input("Ingrese los mpg: "))    
     print("Se consume ",m,"mpg en EEUU")
     aux3 = m*(1609.344)
     aux4 = 1000*(3.785411784)  
     conv1= (aux4/aux3)*100 
     return conv1
i=1
while i == 1:
 print("Seleccione el tipo de conversión:")
 print("0:    l/Km --> mpg")
 print("1:    mpg --> l/Km")
 op = int(input())
 if op == 0:
    c = l100kmtompg()
    print("Se consume ",c,"mpg en EEUU")
 else:
    c1 = mpgtol100km()
    print("Se consume ",c1,"mpg en EEUU")