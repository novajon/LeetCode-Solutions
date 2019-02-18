# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        if t1 == None and t2 == None:
            return None
        
        if t1 == None:
            tree = t2
            
        elif t2 == None:
            tree = t1
            
        else:
            tree = TreeNode(t1.val + t2.val)
            
        
        if t1 != None:
            r = t1.right
            l = t1.left
        else:
            r = None
            l = None
        if t2 != None:
            r1 = t2.right
            l1 = t2.left
        else:
            r1 = None
            l1 = None
            
        tree.left = self.mergeTrees(l,l1)
        tree.right = self.mergeTrees(r,r1)
          
        return tree
