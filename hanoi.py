# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 18:33:01 2021

@author: user
"""

def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        print("moving from %s to %s"%(a,c))
        hanoi(n-1, b, a, c)
        
a=hanoi(100,'a','b','c')