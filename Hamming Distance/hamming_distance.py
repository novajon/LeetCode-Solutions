# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = x ^ y
        count = 0
        while(n):
            count = count + 1
            n &= n-1
            print("n: {}".format(n))
            print("n-1: {}".format(n-1))
        return count


