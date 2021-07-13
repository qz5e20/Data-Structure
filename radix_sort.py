# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 18:31:52 2021

@author: user
"""

def radix_sort(li):
    max_mum=max(li)
    it=0
    while 10**it<=max_mum:
        buckets=[[] for _ in range (10)]
        for var in li:
            digit=(var//10**it)%10
            buckets[digit].append(var)
        
        li.clear()
        for buc in buckets:
            li.extend(buc)
        it+=1
        
import random

li=list(range(1000))
random.shuffle(li)
radix_sort(li)
print(li)
        