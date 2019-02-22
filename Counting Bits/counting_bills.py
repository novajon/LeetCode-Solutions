# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, num: 'int') -> 'List[int]':
        
        bits = []
        
        for i in range(num+1):
            bits.append("{0:b}".format(i).count('1'))
            
        return bits
