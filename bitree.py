# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:36:40 2021

@author: user
"""
from collections import deque

class BittreeNode:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None

a=BittreeNode("A")
b=BittreeNode("B")
c=BittreeNode("C")
d=BittreeNode("D")
e=BittreeNode("E")
f=BittreeNode("F")
g=BittreeNode("G")
h=BittreeNode("H")

e.lchild=a
e.rchild=g
a.rchild=c
c.lchild=b
c.rchild=d
g.rchild=f

root=e

def pre_order(root):
    if root:
        print(root.data,end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)

def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data,end=',')
        in_order(root.rchild)
        
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data,end=',')

def level_order(root):
    queue=deque()
    queue.append(root)
    while len(queue)>0:
        node=queue.popleft()
        print(node.data,end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)
        

        