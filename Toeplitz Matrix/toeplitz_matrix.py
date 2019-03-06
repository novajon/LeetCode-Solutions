# https://leetcode.com/problems/toeplitz-matrix/

from collections import deque
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        # create a queue of elements in first row
        queue = deque(matrix[0])
        # for all other rows
        for row_ind,row in enumerate (matrix[1:]):
            # pop last element in move elements to the right
            queue.pop()
            # append the first element from the new row to the left side
            queue.appendleft(row[0])
            # continue if queue is equal to current row, else return false
            if list(queue) != row:
                return False
        # return True
        return True
