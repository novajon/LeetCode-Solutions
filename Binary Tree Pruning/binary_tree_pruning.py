# https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root.left == None and root.right == None:
            if root.val == 0:
                return None
            else:
                return root
        
        else:
            if root.left != None:
                root.left = self.pruneTree(root.left)
            if root.right != None:
                root.right = self.pruneTree(root.right)
        
        if root.left == None and root.right == None and root.val == 0:
            return None
        else:
            return root
        
