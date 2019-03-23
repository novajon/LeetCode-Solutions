# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root==None:
            return None
        
        elif root.val == val:
            return root
        
        else:
            left = self.searchBST(root.left,val)
            if left != None:
                return left
            else:
                return self.searchBST(root.right,val)
