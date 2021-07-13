# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 21:44:36 2021

@author: user
"""

def bubble_search(li):
    for i in range (len(li)-1):
        exchange=False
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                exchange=True
        if not exchange:
            return

li=[1,5,6,8,9,2,21,48,59,63,48,7]
bubble_search(li)
print(li)
        