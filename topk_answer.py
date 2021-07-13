# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:48:29 2021

@author: user
"""

def sift(li,low,high):
    i=low
    j=2*i+1
    tmp=li[low]
    while j<=high:
        if li[j+1]<li[j] and j+1<=high :
            j+=1
        if li[j]<tmp:
            li[i]=li[j]
            i=j
            j=2*i+1
        else:
            break
    li[i]=tmp

def topk(li,k):
    heap=li[0:k]
    for i in range ((k-2)//2,-1,-1):
        sift(heap, i, k-1)
    for i in range (k,len(li)):
        if li[i]>heap[0]:
            heap[0]=li[i]
            sift(heap, 0, k-1)
    for i in range (k-1,-1,-1):
        heap[0],heap[i]=heap[i],heap[0]
        sift(heap, 0, i-1)
    return heap