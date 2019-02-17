# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for j in J:
            for s in S:
                if s == j:
                    count += 1
        return count
        
