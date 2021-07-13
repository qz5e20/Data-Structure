# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 18:50:32 2021

@author: user
"""

def binary_search(li,val):
    left=0
    right=len(li)-1
    while left <= right:
        mid=(left+right)//2
        if li[mid] == val:
            print(mid)
            return mid
        elif li[mid]>val:
            right=mid-1
        else:
            left=mid+1
    else:
        print("wu")
        return None

li=[1,4,5,6,7,8,9,11,18,23,48]
binary_search(li, 18)