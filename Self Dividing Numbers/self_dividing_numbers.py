# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        numbers = []
        
        #go through range of numbers
        for n in range(left,right+1):
            # test if number is self-dividing
            if self.isSelfDividing(n):
                numbers.append(n)
                
        return numbers
    
    def isSelfDividing(self,number):
        if number < 10:
            return True
        if "0" in str(number):
            return False
        
        for d in str(number):
            if number%int(d) != 0:
                return False
        return True
