# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        curr = 0
        for ind,a in enumerate(A[1:]):
            if a < A[curr]:
                return curr
            else:
                curr = ind + 1
        
        return curr
