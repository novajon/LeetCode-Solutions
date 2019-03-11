# https://leetcode.com/problems/binary-gap/

class Solution:
    def binaryGap(self, N: int) -> int:
        binary = bin(N)[2:]
        dist = 0
        if binary.count("1") <=1:
            return 0
        else:
            start_ind = 0
            max_distance = 0
            for ind,b in enumerate(binary[1:]):
                if b=="1":
                    if (ind+1 - start_ind) > max_distance:
                        max_distance = ind+1-start_ind
                    start_ind = ind+1
        return max_distance
                    
        
