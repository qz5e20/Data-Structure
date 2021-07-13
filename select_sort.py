# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 21:53:56 2021

@author: user
"""

def select_sort(li):
    for i in range (len(li)-1):
        min_loc=i
        for j in range(i+1,len(i)):
            if li[j]<li[min_loc]:
                min_loc=j
            li[i],li[min_loc]=li[min_loc],li[i]