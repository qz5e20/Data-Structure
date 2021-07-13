# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:23:41 2021

@author: user
"""

class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return None
    
    def is_empty(self):
        return len(self.stack)==0

def barce_match(s):
    match={'}':'{',']':'[',')':'('}
    stack=Stack()
    for ch in s:
        if ch in {'(','[','{'}:
            stack.push(ch)
        elif stack.get_top()== match[ch]:
            stack.pop()
        else:
            return False
    if stack.is_empty():
        return True
    else:
        return False
    

print(barce_match('[]'))