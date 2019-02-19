# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> 'int':
        
        # if current node has value, then maximum depth is 1 + the maximum depth of all child nodes
        # recursion base: reached state of no value
        if root == None:
            return 0
        
        # recursion step: find child with maximum depth
        else:
            child_depth = [0]
            for child in root.children:
                child_depth.append(self.maxDepth(child))
            return 1 + max(child_depth)
        
