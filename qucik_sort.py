# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:13:45 2021

@author: user
"""
def partition(li,left,right):
    tmp=li[left]
    while left<right:
        while li[right]>=tmp and left<right:
            right-=1
        li[left]=li[right]
        while li[left]<=tmp and left<right:
            left+=1
        li[right]=li[left]
    li[left]=tmp
    return left
        
def quick_sort(li,left,right):
    if left<right:
        mid=partition(li, left, right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)
        
        
li=[1,7,95,259,484,12,456,89,41,10,25,89,82,74,14,12,12,13,45,48,79]
quick_sort(li, 0, len(li)-1)
print(li)