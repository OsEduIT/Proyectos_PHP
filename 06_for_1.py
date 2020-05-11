# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:23:36 2020

@author: oscar
"""


devices =["R1","R2","R3","S1","S2","S3","S4","R4"]
switches=[]
for i in devices:
    if "S" in i:
          switches.append(i)
print(switches)