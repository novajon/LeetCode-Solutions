# https://leetcode.com/problems/score-after-flipping-matrix/

import copy

class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        
        #boolean to track if a move was made
        move_made = True
        current_score = self.get_score(A)
        
        #as long as another move was made; there is something that we can improve
        while(move_made):
            move_made = False
            #check every possible row and column for improvement
            #row
            for ind in range(len(A)):
                toggled_A = self.toggle_row(A,ind)
                toggled_A_score = self.get_score(toggled_A)
                
                if current_score < toggled_A_score:
                    A = self.toggle_row(A,ind)
                    #move was made
                    move_made = True
                    current_score = self.get_score(A)
                
            for ind,col in enumerate(A[0]):
                toggled_A = self.toggle_column(A,ind)
                toggled_A_score = self.get_score(toggled_A)
                
                if current_score < toggled_A_score:
                    A = self.toggle_column(A,ind)
                    #move was made
                    move_made = True
                    current_score = self.get_score(A)
        return current_score
                    
    
    def get_score(self,A):
        score = 0
        for row in A:
            score += int("".join([str(e) for e in row]),2)
        return score
        
        
    def toggle_column(self,A,ind):
        B = copy.deepcopy(A)
        for r_ind,row in enumerate(A):
            B[r_ind][ind] = abs(A[r_ind][ind]-1)
        return B
    
    
    def toggle_row(self,A,ind):
        B = copy.deepcopy(A)
        for c_ind in range(len(A[ind])):
            B[ind][c_ind] = abs(A[ind][c_ind]-1)
        return B
        
