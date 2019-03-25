# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        split_ind = len(preorder)
        if preorder is None or not preorder:
            return
        root = TreeNode(preorder[0])
        
        #find next bigger element
        for ind,i in enumerate(preorder):
            if i>root.val:
                split_ind = ind
                break
        
        root.left = self.bstFromPreorder(preorder[1:split_ind])
        if split_ind!=len(preorder):
            root.right = self.bstFromPreorder(preorder[split_ind:])
        
        return root    
        
