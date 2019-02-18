# https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, A: 'List[int]') -> 'List[int]':
        neg_log = []
        pos_log = []
        reit = True
        while(reit):
            reit = False
            for i,a_i in enumerate(A):
                if i%2 == a_i%2:
                    continue
                elif i%2 == 1:
                    pos_log.append(a_i)
                    if neg_log:
                        A[i] = neg_log[0]
                        neg_log.pop(0)
                    else:
                        reit=True
                else:
                    neg_log.append(a_i)
                    if pos_log:
                        A[i] = pos_log[0]
                        pos_log.pop(0)
                    else:
                        reit=True
        return A
