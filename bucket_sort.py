# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:23:41 2021

@author: user
"""
import random

def bucket_sort(li,n=100,max_num=10000): #100个捅 最大 10000个数
    buckets=[[] for _ in range(n)]
    for var in li:
        i=min(var//(max_num//n),n-1) #min是方便当值为10000将第一万放入第99个捅
        #对这两者取个最小值
        buckets[i].append(var)
        #保持桶内顺序
        for j in range(len(buckets[i])-1,0,-1):
            if buckets[i][j]<buckets[i][j-1]:
                buckets[i][j],buckets[i][j-1]=buckets[i][j-1],buckets[i][j]
            else:
                break
    sorted_li=[]
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li

li=[random.randint(0,10000) for i in range(100)]

li=bucket_sort(li)

print(li)