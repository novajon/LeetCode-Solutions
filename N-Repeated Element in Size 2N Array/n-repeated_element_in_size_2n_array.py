# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        dic = []
        for el in A:
            if el in dic:
                return el
            else: 
                dic.append(el)
        
