# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:01:24 2020

@author: oscar
"""


def crearlistas(n):
    mylist=[]
    for i in range(1,n+1,3):
        mylist.append(i)
    return mylist
print(crearlistas(100))    