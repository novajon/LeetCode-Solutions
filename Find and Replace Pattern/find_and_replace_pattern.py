# https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
        matches = []
        
        for word in words:
            if len(word) != len(pattern):
                continue
            perm = {}
            for ind,letter in enumerate(word):
                if pattern[ind] not in perm.keys() and letter not in perm.values():
                    perm[pattern[ind]] = letter
                elif pattern[ind] not in perm.keys() and letter in perm.values():
                    break
                elif perm[pattern[ind]] != letter:
                    break

                if ind == len(word) - 1:
                    matches.append(word)
        
        return matches
