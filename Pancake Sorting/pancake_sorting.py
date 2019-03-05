# https://leetcode.com/problems/pancake-sorting/

# this is not the most performant solution for this problem; but the first I came up with when solving this problem.
# A further analysis of this problem is done in https://people.eecs.berkeley.edu/~christos/papers/Bounds%20For%20Sorting%20By%20Prefix%20Reversal.pdf

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        moves = []
        
        while not self.isSorted(A):
            print(A)
            # search for largest element and move it over to the left (flip point should be the index of the largest element)
            highest_index = self.getHighestIndex(A)
            A_new = self.flipOnIndex(A,highest_index)
            moves.append(highest_index)

            # then perform a flip in A.length to move that element to the end of the array
            A_new = self.flipOnIndex(A_new,len(A_new))
            moves.append(len(A_new))
            
            # repeat the procedure without the last element in A
            A = A_new [:-1]
        print(A)
        return moves
    
    
    def flipOnIndex(self,A,index):
        return A[index-1::-1] + A[index:]
    
    def getHighestIndex(self,A):
        return A.index(max(A))+1
        
    def isSorted(self,A):
        return all(A[i] <= A[i+1] for i in range(len(A)-1))
        
