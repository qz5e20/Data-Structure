# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:17:09 2021

@author: user
"""

def count_sort(li,max_count=100):
    count=[0 for _ in range(max_count)]
    for val in li:
        count[val]+=1
    li.clear()
    for ind,val in enumerate(count):
        for i in range (val):
            li.append(ind)
            
li=[1,1,5,5,8,8,6,6,7,8,7,9,8,9,85,15,15,78,89,78,48,15,15,16,23,23,25]
count_sort(li)
print(li)
    