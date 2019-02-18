# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        #array to save unclosed brackets
        open_brackets = 0
        lost_brackets = 0
        
        #loop through array
        for bracket in S:
            if bracket == "(":
                    open_brackets +=1
            else:                
                if open_brackets>0:
                    open_brackets -= 1
                else:
                    lost_brackets +=1
    
        #count length of unclosed array
        return open_brackets + lost_brackets
