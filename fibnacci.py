# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 23:58:54 2021

@author: user
"""

def fibnacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibnacci(n-1)+fibnacci(n-2)

print(fibnacci(10))


def fibnacci_no_recurision(n):
    f=[0,1,1]
    if n>2:
        for i in range (n-2):
            num = f[-1]+f[-2]
            f.append(num)
    return f[n]
        
#第一个慢第二个块，递归效率比较慢，子问题的重复计算
#下部分就是动态规划
#最优子结构=递推式+重复子问题
#python可以再递归前加@lru_cache就能自动缓存子问题的部分


