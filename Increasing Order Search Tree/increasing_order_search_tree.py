# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        # traverse tree to get ordered list
        def traverseTree(root):
            traversal = []
            if root.left:
                traversal.extend(traverseTree(root.left))
            traversal.append(root.val)
            if root.right:
                traversal.extend(traverseTree(root.right))
            return traversal
        ordered_list = traverseTree(root)
        
        # create output tree
        output_tree = TreeNode(ordered_list[0])
        temp = output_tree
        for el in ordered_list[1:]:
            temp.right = TreeNode(el)
            temp = temp.right
        
        return output_tree
