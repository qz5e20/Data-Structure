# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:05:50 2021

@author: user
"""

def insert_sort(li):
    for i in range (1,len(li)):
        tmp=li[i]
        j=i-1
        while li[j]>tmp and j>=0:
            li[j+1]=li[j]
            j-=1
        li[j+1]=tmp
        
li=[1,5,8,7,1,3,6,4,8,7,12,46,8,2]
insert_sort(li)
print(li)