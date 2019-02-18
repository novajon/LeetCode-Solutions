# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        for ind,a in enumerate(A[::-1]):
            if a >= 0:
                A[ind] = a ** 2
            else:
                
        A.sort()
        
        return A
