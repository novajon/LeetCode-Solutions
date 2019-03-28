# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        
        for n in range(N+1):
            n_format = "{0:b}".format(n)
            if n_format not in S:
                return False
            
        return True
