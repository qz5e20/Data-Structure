# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:07:45 2021

@author: user
"""

    


#支持分数
class Fraction:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        x=self.gcd2(a,b)
        self.a/=x
        self.b/=x
    
    def gcd(self,a,b):
        if b==0:
            return a
        else:
            return self.gcd(b,a%b)
    #伪递归，与循环差不多
    
    def zgs(self,a,b):
        x=self.gcd(a,b)
        return a*b/x

    def __add__(self,other):
        a=self.a
        b=self.b
        c=other.a
        d=other.b
        fenmu=self.zgs(b,d)
        fenzi=a*fenmu/b+c*fenmu/d
    
    def __str__(self):
        return "%d%d"%(self.a,self.b)
    
    def gcd2(self,a,b):
        while b>0:
            r=a%b
            a=b   #可以写成 a,b=b,a%b
            b=r
        return a

a=Fraction(30, 15)    
b=Fraction(1, 2)
print(a+b)