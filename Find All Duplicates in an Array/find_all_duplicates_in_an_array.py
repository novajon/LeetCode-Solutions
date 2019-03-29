# https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        output = []
        exists = {}
        
        for ind,num in enumerate(nums):
            if num in exists:
                output.append(num)
            else:
                exists[num] = True
            
        
        return output
