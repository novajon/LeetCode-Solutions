# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import copy
class Solution:
    def middleNode(self, head: 'ListNode') -> 'ListNode':
        
        final_node = head
        current = head.next
        change = True
        
        while current != None:
            if change:
                final_node = final_node.next
                change  = False
            else:
                change = True
            current = current.next
            
        return final_node
            
        
