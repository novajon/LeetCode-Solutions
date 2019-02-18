# https://leetcode.com/problems/array-partition-i/

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        sum = 0
        for n in nums[0::2]:
            sum+= n
        
        return sum
