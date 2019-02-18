# https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        
        #check if all columns have same length? - assuming this is not relevant
        
        #counter of deletions
        counter = 0
        
        # for each column in A:
        for col_ind, _ in enumerate (A[0]):
        # check if column is sorted:
            start = A[0][col_ind]
            for a in A:
                # if not sorted:
                    if a[col_ind] < start:
                        # increase counter
                        counter += 1
                        break
                # else:
                    else:
                        start = a[col_ind]
        return counter
        
