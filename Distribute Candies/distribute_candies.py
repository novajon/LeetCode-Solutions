# https://leetcode.com/problems/distribute-candies/

from collections import Counter

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        
        #count occurences and assign candy to sister to be as diverse as possible
        counts = Counter(candies)
        total_candy = len(candies)
        candy_each = total_candy/2

        if len(counts.keys()) > candy_each:
            return int(candy_each)
        else:
            return len(counts.keys())
