# https://leetcode.com/problems/reshape-the-matrix/

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        if nums and len(nums) > 0 and len(nums)*len(nums[0]) == r*c:
            new_matrix = []
            new_row = []
            for r_ind,row in enumerate(nums):
                for c_ind,col in enumerate(row):
                    if len(new_row) == c:
                        new_matrix.append(new_row)
                        new_row = [col]
                    else:
                        new_row.append(col)
            new_matrix.append(new_row)
            return new_matrix
        else:
            return nums
