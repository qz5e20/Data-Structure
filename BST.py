# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:17:08 2021

@author: user
"""

class BittreeNode:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
        self.parent=None
        
    
class BST:
    def __init__(self,li=None):
        self.root=None
        if li:
            for val in li:
                self.insert_no_rec(val)
                
    def insert(self,node,val):
        if not node:
            node=BittreeNode(val)
        elif val<node.data:
            node.lchild=self.insert(node.lchild, val)
            node.lchild.parent=node
        elif val>node.data:
            node.rchild=self.insert(node.rchild, val)
            node.rchild.parent=node
        #相等就不要了
        return node
        
    def insert_no_rec(self,val):
        p=self.root
        if not p:
            self.root=BittreeNode(val)
            return
        while True:
            if val<p.data:
                if p.lchild:
                    p=p.lchild
                else:
                    p.lchild=BittreeNode(val)
                    p.lchild.parent=p
                    return
            elif val>p.data:
                if p.rchild:
                    p=p.rchild
                else:
                    p.rchild=BittreeNode(val)
                    p.rchild.parent=p
                    return
            else:
                return
    
    def query(self,node,val):
        if not node:
            return None
        elif node.data<val:
            return node.query(node.rchild,val)
        elif node.data>val:
            return node.query(node.lchild,val)
        else:
            return node
    
    def query_no_rec(self,val):
        p=self.root
        while p:
            if p.data<val:
                p=p.rchild
            elif p.data>val:
                p=p.lchild
            else:
                return p
        return None
    
    def pre_order(self,root):
        if root:
            print(root.data,end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self,root):
        if root:
            self.in_order(root.lchild)
            print(root.data,end=',')
            self.in_order(root.rchild)
        
    def post_order(self,root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data,end=',')
    
    
    def __remove_node_1(self,node):
        if not node.parent:
            self.root=None
        elif node==node.parent.lchild:
            node.parent.lchild=None
        else:
            node.parent.rchild=None
    
    def __remove_node_21(self,node):
        #只有一个左孩子
        if not node.parent:
            self.root=node.lchild
            node.lchild.parent=None
        elif node==node.parent.lchild:
            node.parent.lchild=node.lchild
            node.lchild.parent=node.parent
        else:
            node.parent.rchild=node.lchild
            node.lchild.parent=node.parent
                 
    def __remove_node_22(self,node):
        #node只有一个右孩子
        if not node.parent:
            self.root=node.rchild
            node.rchild.parent=None
        elif node==node.parent.lchild:
            node.parent.lchild=node.rchild
            node.rchild.parent=node.parent
        else:
            node.parent.rchild=node.rchild
            node.rchild.parent=node.parent
            
    def delete(self,val):
        if self.root:
            node =self.query_no_rec(val)
            if not node:
                return False
            if not node.lchild and not node.rchild:
                self.__remove_node_1(node)
            elif not node.rchild:
                self.__remove_node_21(node)
            else:
                min_node=node.rchild
                while min_node.lchild:
                    min_node=min_node.lchild
                node.data=min_node.data
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)
    
tree=BST([4,6,7,9,2,1,3,5,8])
print("")
tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)
print("")
tree.post_order(tree.root)
print(tree.query_no_rec(10))
tree.delete(4)
tree.pre_order(tree.root)


                    