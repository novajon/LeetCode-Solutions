#  https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        out = []
        
        for search_key in nums1:
            compare_array = nums2[nums2.index(search_key) + 1:]
            next_larger = -1
            for c in compare_array:
                if c > search_key:
                    next_larger = c
                    break
            out.append(next_larger)
        
        return out
                
