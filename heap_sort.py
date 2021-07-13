# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:27:50 2021

@author: user
"""

def sift(li,low,high):
    i=low
    j=2*i+1
    tmp=li[low]
    while j<=high:
        if li[j+1]>li[j] and j+1<=high :
            j+=1
        if li[j]>tmp:
            li[i]=li[j]
            i=j
            j=2*i+1
        else:
            break
    li[i]=tmp
    
def heap_sort(li):
    n=len(li)
    for i in range ((n-2)//2,-1,-1):
        sift(li, i, n-1)
    for i in range (n-1,-1,-1):
        li[0],li[i]=li[i],li[0]
        sift(li, 0, i-1)
    
li=[2,5,87,789,48,1,4,8,9,6,169,15,874,85,12,45,78,98,95,62,45,12,48,78,79]
heap_sort(li)
print(li)