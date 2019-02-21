# https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, A: 'List[List[int]]') -> 'List[List[int]]':
        
        B = [[A[r_el][c_el] for r_el in range(len(A))] for c_el in range(len(A[0]))]   
        
        return B
