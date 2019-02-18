# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> 'List[int]':
        return self.preorder_iterative(root)

    def preorder_iterative(self, root: 'Node') -> 'List[int]':
    if root != None:
        return []
    
    pre_list = [root.val]
    exists_children=False
    
    if root.children != None:
        exists_children = True
    
    while exists_children:
        
        
    
    if root != None:
        pre_list.append(root.val)

        for child in root.children:
            res = self.preorder(child)
            pre_list.extend(res)

    return pre_list
    
    def preorder_recursive(self, root: 'Node') -> 'List[int]':
        pre_list = []
        
        if root != None:
            pre_list.append(root.val)
        
            for child in root.children:
                res = self.preorder(child)
                pre_list.extend(res)

        return pre_list
