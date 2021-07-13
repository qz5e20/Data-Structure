# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:30:08 2021

@author: user
"""
from BST import BST,BittreeNode

class AVLNode(BittreeNode):
    def __init__(self,data):
        BittreeNode.__init__(self,data)
        self.bf=0
        
class AVLtree(BST):
    def __init__(self,li=None):
        BST.__init__(self,li)
    
    def rotate_left(self,p,c):
        s2=c.lchild
        p.rchild=s2
        if s2:
            s2.parent=p
        c.lchild=p
        p.parent=c
        p.bf=0
        c.bf=0
        return c
    
    def rotate_right(self,p,c):
        s2=c.rchild
        p.lchild=s2
        if s2:
            s2.parent=p
        c.rchild=p
        p.parent=c
        p.bf=0
        c.bf=0
        return c
    
    def rotate_right_left(self,p,c):
        g=c.lchild
        
        s3=g.rchild
        c.lchild=s3
        if s3:
            s3.parent=c
        g.rchild=c
        c.parent=g
        
        s2=g.lchild
        p.rchild=s2
        if s2:
            s2.parent=p
        g.lchild=p
        p.parent=g
        
        if g.bf>0:
            p.bf=-1
            c.bf=0
        elif g.bf<0:
            p.bf=0
            c.bf=1
        else:
            p.bf=0
            c.fb=0
        return g

    def rotate_left_right(self,p,c):
        g=c.rchild
        
        s2=g.lchild
        c.rchild=s2
        if s2:
            s2.parent=c
        g.lchild=c
        c.parent=g
        
        s3=g.rchild
        p.lchild=s3
        if s3:
            s3.parent=p
        g.rchild=p
        p.parent=g
        
        if g.bf<0:
            p.bf=1
            c.bf=0
        elif g.bf>0:
            p.bf=0
            c.bf=-1
        else:
            p.bf=0
            c.fb=0
        return g
    
    def insert_no_rec(self,val):
        p=self.root
        if not p:
            self.root=AVLNode(val)
            return
        while True:
            if val<p.data:
                if p.lchild:
                    p=p.lchild
                else:
                    p.lchild=AVLNode(val)
                    p.lchild.parent=p
                    node=p.lchild
            elif val>p.data:
                if p.rchild:
                    p=p.rchild
                else:
                    p.rchild=AVLNode(val)
                    p.rchild.parent=p
                    node=p.rchild
                    break
            else:
                return
            
        while node.parent:
            if node.parent.lchild==node: #左子树来的
            #更新bf
                if node.parent.bf<0:
                    #看node哪边沉
                    g=node.parent.parent #为了连接旋转之后的子树
                    x=node.parent#旋转前的子树的根
                    if node.bf>0:
                        n=self.rotate_left_right(node.parent,node)
                    else:
                        n=self.rotate_right(node.parent, node)
                        #记得把n和g连起来
                elif node.parent.bf>0:
                    node.parent.bf=0
                    break
                else:
                        node.parent.bf=-1
                        node=node.parent
                        continue
            else:#右子树来的
                if node.parent.bf>0:
                    g=node.parent.parent 
                    x=node.parent
                    if node.bf<0:
                        n=self.rotate_right_left(node.parent,node)
                    else:
                        n=self.rotate_left(node.parent, node)
                        
                elif node.parent.bf<0:
                    node.parent.bf=0
                    break
                else:
                    node.parent.bf=1
                    node=node.parent
                    continue
                #链接旋转后的子树
            n.parent=g
            if g:
                if x==g.lchild:
                    g.lchild=n
                else:
                    g.rchild=n
                break
            else:
                self.root=n
                break

tree =AVLtree([9,8,7,6,5,4,3,2,1])

tree.pre_order(tree.root)
