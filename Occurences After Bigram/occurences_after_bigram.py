# https://leetcode.com/problems/occurrences-after-bigram/

class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        
        text = text.split(" ")
        matches = []
        
        if first in text and second in text:
            for ind, word in enumerate(text):
                if word == first:
                    if ind < len(text)-2:
                        if text[ind+1] == second:
                            matches.append(text[ind+2])
                        
        return matches
