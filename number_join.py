# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:32:20 2021

@author: user
"""
from functools import cmp_to_key

li =[32,94,128,1286,6,71]
def xy_cmp(x,y):
    if x+y>y+x:
        return 1
    elif x+y<y+x:
        return -1
    else:
        return 0

def number_join(li):
    li=list(map(str(li))) #map是列表中每一个数过一遍里面这个函数str，转字符串
    li.sort(key=cmp_to_key(xy_cmp))
    return "".join(li)

