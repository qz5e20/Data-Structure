# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 18:27:08 2021

@author: user
"""

class LinkList:
    class Node: 
        def __init__(self,item=None):
            self.item=item
            self.next=None
    
    class LinListIterator:
        def __init__(self,node):
            self.node=node
       
        def __next__(self):
            if self.node:
                cur_node=self.node
                self.node=cur_node.next
                return cur_node.item
            else:
                raise StopIteration
        
        def __iter__(self):
            return self
        
    def __init__(self,iterable=None):
        self.head=None
        self.tail=None
        if iterable:
            self.extend(iterable)
                
    def append(self,obj):
        s=LinkList.Node(obj)
        if not self.head:
            self.head=s
            self.tail=s
        else:
            self.tail.next=s
            self.tail=s
                
    def extend(self,iterable):
        for obj in iterable:
            self.append(obj)
        
    def find(self,obj):
        for n in self:
            if n==obj:
                return True
            else:
                return False
    def __iter__(self):
        return self.LinListIterator(self.head) #使他能个迭代
    def __repr__(self):
        return "<<"+",".join(map(str, self))+">>" #map转化为字符串
        
class HashTable:
    def __init__(self,size=101):
        self.size=size
        self.T=[LinkList() for i in range(self.size)]
        
    def h(self,k):
        return k%self.size
    
    def insert(self,k):
        i=self.h(k)
        if self.find(k):   #去重
            print("Duplicated Insert")
        else:
            self.T[i].append(k)
        
    def find(self,k):
        i=self.h(k)
        print(self.T[i])
        return self.T[i].find(k)
    
ht=HashTable()

ht.insert(0)        
ht.insert(1)    
ht.insert(3)    
ht.insert(102)    
ht.insert(508)    
ht.insert(403)   
ht.insert(14) 
ht.insert(48)
ht.insert(8)
ht.insert(38)
ht.insert(101)
ht.insert(101)
 

print(",".join(map(str, ht.T)))
print (ht.find(101))
          
        
        
    