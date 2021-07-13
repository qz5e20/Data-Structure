# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 23:43:17 2021

@author: user
"""
from collections import deque 

maze=[
      [1,1,1,1,1,1,1,1,1,1],
      [1,0,0,1,0,0,0,1,0,1],
      [1,0,0,1,0,0,0,1,0,1],
      [1,0,0,0,0,1,1,0,0,1],
      [1,0,1,1,1,0,0,0,0,1],
      [1,0,0,0,1,0,0,0,0,1],
      [1,0,1,0,0,0,1,0,0,1],
      [1,0,1,1,1,0,1,1,0,1],
      [1,1,0,0,0,0,0,0,0,1],
      [1,1,1,1,1,1,1,1,1,1]
]

dirs=[
      lambda x,y:(x+1,y),
      lambda x,y:(x-1,y),
      lambda x,y:(x,y+1),
      lambda x,y:(x,y-1)
]

def print_r(path):
    curNode=path(-1)
    realpath=[]
    while curNode[2]!=-1:
        realpath.append(curNode[0:2])
        curNode=path[curNode[2]]        
    realpath.append(curNode[0:2])
    realpath.reverse()
    for node in realpath:
        print(node)
        
def maze_path_queue(x1,y1,x2,y2):
    queue=deque()
    queue.append((x1,y1,-1))
    path=[]
    while len(queue)>0:
        curNode=queue.popleft()
        path.append(curNode)
        if curNode[0]==x2 and curNode[1]==y2:
            print_r(path)
            return True
        for dir in dirs:
            nextNode=dir(curNode[0],curNode[1])
            if maze[nextNode[0]][nextNode[1]]==0:
                queue.append((nextNode[0],nextNode[1],len(path)-1))
                maze[nextNode[0]][nextNode[1]]=2
    else:
        print("no way")
        return False
        
maze_path_queue(2, 1, 8, 8)