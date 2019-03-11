# https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        # get value sequence for root1 and root2
        seq1 = self.getValueSequence(root1)
        seq2 = self.getValueSequence(root2)
        
        # check if value sequences are equal
        return seq1 == seq2
    
    def getValueSequence(self,root):
        seq = []
        if root.left != None:
            seq.extend(self.getValueSequence(root.left))
        if root.right != None:
            seq.extend(self.getValueSequence(root.right))
        if root.left == None and root.right == None:
            seq.append(root.val)
        return seq
