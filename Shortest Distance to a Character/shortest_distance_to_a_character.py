# https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        #distance_list
        distance_list = []
        
        # get occurence indices for letter C
        occurence_indices = [ind for ind,el in enumerate(S) if el==C]
        
        # go through indices and add the minimum to any index from the list above
        for ind,el in enumerate(S):
            distance_list.append(min([abs(ind-oc_ind) for oc_ind in occurence_indices]))
            
        return distance_list
