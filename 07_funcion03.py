# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:53:42 2020

@author: oscar
"""

def hola3(lista):
    for a in lista:
        print("Hola ",a)
        return lista

mylista = ["Oscar", "Majo","Neron","Shorty"]
hola3(["Oscar","Majo"])
hola3(["Oscar","Majo","Eduardo","David","Pepe"])
hola3(["Juan"])
hola3((1,2,2.5,3.8,"Majo",True))
print(hola3(mylista))       