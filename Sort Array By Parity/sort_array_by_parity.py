# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        odd_numbers = []
        even_numbers = []
        
        for el in A:
            if el % 2==0:
                even_numbers.append(el)
            else:
                odd_numbers.append(el)
        
        even_numbers.extend(odd_numbers)
        
        return even_numbers
