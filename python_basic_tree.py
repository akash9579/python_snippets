# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 18:11:17 2021

@author: 91937
"""


class treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
        
    def add_children(self,child):
        child.parent=self
        self.children.append(child)
        
    def print_tree(self):
        print(self.data)
        for ele in self.children:
            print(ele.print_tree())
        
       
        
        
        
        

root = treenode("president")
parshuram = treenode("parshuram")
root.add_children(parshuram)
root.add_children(treenode("parshuram1"))
root.add_children(treenode("parshuram2"))

root.print_tree()