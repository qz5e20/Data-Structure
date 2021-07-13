# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 16:24:04 2021

@author: user
"""

class Node:
    def __init__(self.item):
        self.item=item
        self.next=None

a=Node(1)
b=Node(2)
c=Node(3)

a.next=b
b.next=c

def creat_linlist_head(li):
    head =Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next=head
        head=node
    return head

def creat_linlist_tail(li):
    head=Node(li[0])
    tail=head
    for element in li[1:]:
        node = Node(element)
        tail.next=node
        tail=node
    return head
        
def print_linlist(lk):
    while lk:
        print(lk.item,end=',')
        li=li.next
        
lk=creat_linlist_head([1,2,3])
