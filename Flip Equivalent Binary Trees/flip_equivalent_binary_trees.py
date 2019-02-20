# https://leetcode.com/problems/flip-equivalent-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: 'TreeNode', root2: 'TreeNode') -> 'bool':
        
        if root1 == root2 == None:
            return True
        
        elif root1 == None or root2 == None:
            return False
        
        # go through one tree
        if root1.val != root2.val:
            return False
        
        # check if both children are contained in the other tree
        
        # check if they have a different number of subtrees
        if [root1.left,root1.right].count(None) != [root2.left,root2.right].count(None):
            return False
        
        # return true when reached a leave
        elif [root1.left,root1.right].count(None) == 2:
                return True
        
        m1 = self.flipEquiv(root1.left,root2.left)
        m2 = self.flipEquiv(root1.left,root2.right)
        m3 = self.flipEquiv(root1.right,root2.left)
        m4 = self.flipEquiv(root1.right,root2.right)
        
        return (m1 or m2) and (m3 or m4)
