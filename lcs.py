# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 19:01:06 2021

@author: user
"""

def lcs_length(x,y):
    m=len(x)
    n=len(y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            
            if x[i-1]==y[j-1]:   #i,j位置上的字符匹配的时候，来自于左上方+1   
                c[i][j]=c[i-1][j-1]+1
            else:
                c[i][j]=max(c[i-1][j],c[i][j-1])
    for _ in c:
        print(_)
    return c[m][n]

#print(lcs_length("ABAVCACAC", "AVABAAA"))

def lcs(x,y):
    m=len(x)
    n=len(y)
    c=[[0 for _ in range(n+1)] for _ in range(m+1)]
    b=[[0 for _ in range(n+1)] for _ in range(m+1)] #1左上方 2上方 3左方
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:   #i,j位置上的字符匹配的时候，来自于左上方+1   
                c[i][j]=c[i-1][j-1]+1
                b[i][j]=1
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
                b[i][j]=2
            else:
                c[i][j]=c[i][j-1]
                b[i][j]=3
        return c[m][n],b
                
def lcs_trackback(x,y):
    c,b=lcs(x,y)
    i=len(x)
    j=len(y)
    res=[]
    while j>0 and j>0:
        if b[i][j]==1:
            res.append(x[i-1])
            j-=1
            i-=1
        elif b[i][j]==2:
            i-=1
        else:
            j-=1
    return"".join(reversed(res))

print(lcs_trackback("ABCDSDSD", "BBYCAYB"))
    
    