# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:53:03 2021

@author: 97250
"""

class Node():
    
    """
    Info: The following is the definition of Binary Search Tree(BST) according to Wikipedia
    Binary Search Tree is a node-based binary tree data structure which has the following properties:  

    The left subtree of a node contains only nodes with keys lesser than the node’s key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    The left and right subtree each must also be a binary search tree. 
    There must be no duplicate nodes.
    
    https://en.wikipedia.org/wiki/Binary_search_tree
    """
    
    def __init__(self, value):
        
        self.value = value
        
        self.left = None
        self.right = None
        
    def get_left(self):
        pass
    
    def get_right(self):
        pass
    
    def set_left(self, other):
        pass
    
    def set_right(self, other):
        pass
    
    def set_value(self, value):
        self.value = value
        
        return True
    
    def get_value(self):
        return self.value
    
    def add_node(self, root, key):
        
        """
        Info: Now let’s transform this binary tree into a binary search tree, 
        implement a function add_node(node) and add it to the three, 
        make sure you respect all the conditions of the binary search tree 
        (the node needs to be added at the right place, depending on its value).
        """
        
        if root is None:
            return Node(key)
        else:
            if root.value == key:
                return root
            elif root.value < key:
                root.set_right(add_node(root.get_right(), key))
            else:
                root.left = insert(root.left, key)
        return root
    
    def search(root, key):
        
        """
        Info: Implement a method search(value) which return the node containing
        this value inside the tree.
        """
        
        # Base Cases: root is null or key is present at root
        if root is None or root.value == key:
            return root
 
        # Key is greater than root's key
        if root.value < key:
            return search(root.get_right(), key)
   
        # Key is smaller than root's key
        return search(root.get_left(), key)