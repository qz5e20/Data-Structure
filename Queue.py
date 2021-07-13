# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 23:20:15 2021

@author: user
"""

class Queue:
    def __init__(self,size=100):
        self.queue=[0 for _ in range(size)]
        self.size=size
        self.rear=0
        self.front=0
    
    def is_filled(self):
        return (self.rear+1)%self.size==self.front
   
    def is_empty(self):
        return self.rear==self.front
    
    def push(self,element):
        if not self.is_filled():
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=element
        else:
            raise IndexError("Queue is filled")
            
    def pop(self):
        if not self.is_empty():
            self.front=(self.front+1)%self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queen is empty")
            
#deque等内置模块可以用队列的