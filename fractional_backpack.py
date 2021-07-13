# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 22:58:26 2021

@author: user
"""
goods=[(60,10),(100,20),(120,30)]
goods.sort(key=lambda x:x[0]/x[1],reverse=True)

def fractional_backpack(goods,w):
     
     m=[0 for _ in range(len(goods))]
     total_v=0
     for i,(prize,weight) in enumerate(goods):
         if w>=weight:
             m[i]=1
             total_v+=prize
             w-=weight
         else:
             m[i]=w/weight
             total_v+=m[i]*prize
             w=0
             break
         print(total_v)
         print(m)
    
     return m,total_v
     

     
     
fractional_backpack(goods, 50)

    