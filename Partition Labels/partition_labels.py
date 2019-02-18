# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        all_lists = []
        while (S):
            ind = 0
            # add first element to list
            curr_list = S[0]

            # search array for last occurence of same character
            unknown_elements = True
        
            while(unknown_elements):
                for el_ind,el in enumerate(S[::-1]):
                    if el in curr_list:
                        temp_ind = len(S)-1-el_ind
                        if temp_ind == ind:
                            unknown_elements = False
                            S = S[temp_ind+1:]
                            all_lists.append(curr_list)
                        else:
                            curr_list = S[0:temp_ind+1]
                        ind = temp_ind
                        break
        
        return [len(x) for x in all_lists]
        
        # include all characters in between to array
        
        # continue searching after last occurence of same character until finding last character from all current characters
        
        #repeat above
        
        
        
