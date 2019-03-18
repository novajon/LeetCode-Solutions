# https://leetcode.com/problems/daily-temperatures/

class Solution: 

    # look ahead for next higher temperature

    # could be implemented more efficiently (less individual edge case tests)

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        next_temp = []
        for ind_t, t in enumerate(T):
            next_found = False
            next_ind=0
            if len(T[ind_t+1:])>0:
                while not next_found:
                    if T[ind_t+1:][next_ind]>t:
                        next_temp.append(next_ind+1)
                        next_found = True
                    else:
                        next_ind +=1
                        if next_ind >= len(T[ind_t+1:]):
                            next_temp.append(0)
                            next_found = True
            else:
                next_temp.append(0)
        return next_temp
            
