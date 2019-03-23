# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        open_remaining = 0
        closing_remaining = 0
        
        for bracket in S:
            if bracket == "(":
                open_remaining+=1
            if bracket == ")":
                if open_remaining>0:
                    open_remaining-=1
                else:
                    closing_remaining+=1
                
        return open_remaining + closing_remaining
