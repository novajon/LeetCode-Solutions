# https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        for ind,image in enumerate(A):
            new_image = []
            for img_ind,el in enumerate(image[::-1]):
                new_image.append(abs(el - 1))
            A[ind] = new_image
    
        return A
    
        
