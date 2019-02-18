# https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        N = [i for i in range(len(S)+1)]
        final = []
        
        for s in S:
        # select highest number possible when decreasing
            if s == "D":
                final.append(max(N))
                N.remove(max(N))

            # select lower number possible when increasing
            else:
                final.append(min(N))
                N.remove(min(N))
        final.append(N[0])

        return final

        
