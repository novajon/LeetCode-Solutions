# https://leetcode.com/problems/custom-sort-string/

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        
        indices = []
        # for each element in T:
        for t in T:
            if t in S:
                # get index in S
                indices.append(S.index(t))
            else:
                indices.append(27)
            
            
        # sort T according to indices
        return "".join([x for _, x in sorted(zip(indices,T), key=lambda pair: pair[0])])
        
