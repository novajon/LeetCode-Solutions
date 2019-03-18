https://leetcode.com/problems/daily-temperatures/

class Solution:

    def dailyTemperaturesLookBack(self, T: List[int]) -> List[int]:
        
        # unresolved indices
        unresolved = []
        next_hot_day = [0 for t in T]
        
        for ind,t in enumerate(T):
            u_ind = 0
            while u_ind < len(unresolved):
                u = unresolved[u_ind]
                if T[u]<t:
                    next_hot_day[u] = ind-u
                    del unresolved[u_ind]
                    u_ind -= 1
                u_ind +=1
            unresolved.append(ind)

        return next_hot_day
