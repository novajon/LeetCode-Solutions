# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if L < R:
            small = L
            large = R
        else: 
            small = R
            large = L
        
        sum = 0
        
        if root.left != None:
            sum += self.rangeSumBST(root.left,L,R)
        
        if root.right != None:
            sum += self.rangeSumBST(root.right,L,R)
        
        if root.val >= small and root.val <= large:
            sum += root.val
        
        return sum
        
        
