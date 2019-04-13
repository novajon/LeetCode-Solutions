# https://leetcode.com/problems/camelcase-matching/

import re

class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        
        # create regex from pattern
        regex = "^[a-z]*"
        for letter in pattern:
            regex+= letter + "[a-z]*"
        
        regex+= "$"
        
        # match regex to each query
        truth_values = []
        for query in queries:
            truth_values.append(re.search(regex,query))
        
        return truth_values
