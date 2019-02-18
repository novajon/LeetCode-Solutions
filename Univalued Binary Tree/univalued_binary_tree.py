# https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: 'TreeNode') -> 'bool':
        return self.isUnivalTreeGivenNumber(root, root.val)
    
    def isUnivalTreeGivenNumber(self, root, number):
        
        if root.val != number:
            return False
        
        elif root.left == None and root.right == None:
            return True
        
        else:
            right_root = True
            left_root = True
            if root.left != None:
                left_root = self.isUnivalTreeGivenNumber(root.left,number)
            if root.right != None:
                right_root = self.isUnivalTreeGivenNumber(root.right,number)
            
            return right_root and left_root
        
