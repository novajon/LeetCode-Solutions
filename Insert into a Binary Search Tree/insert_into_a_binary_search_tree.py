# https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        if root == None:
            lt = TreeNode(val)
            return lt
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        elif val > root.val:
            root.right =  self.insertIntoBST(root.right,val)
        
        return root
