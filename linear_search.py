# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 18:40:41 2021

@author: user
"""

def linear_search(li,val):
    for ind,v in enumerate(li):
        if v==val:
            print(ind)
            return ind
    else:
        print("wu")
        return None
        
li=[1,2,3,4,6,8,9,10]

linear_search(li,3)