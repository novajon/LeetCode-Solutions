# https://leetcode.com/problems/distribute-candies/

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        
        #count occurences and assign candy to sister to be as diverse as possible
        indvs = len(set(candies))
        candy_each = int(len(candies)/2)

        if indvs > candy_each:
            return int(candy_each)
        else:
            return indvs
