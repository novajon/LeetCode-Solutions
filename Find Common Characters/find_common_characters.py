# https://leetcode.com/problems/find-common-characters/

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        shortest_word = A[0]
        final=[]
        
        for ch in set(shortest_word):
            count = shortest_word.count(ch)
            for a in A[1:]:
                count=min(count,a.count(ch))
            for c in range(count):
                final.append(ch)
        
        return final
                
                
                
        
