# https://leetcode.com/problems/baseball-game/

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        curr_score = 0
        valid_rounds = []
        
        for ind,op in enumerate(ops):
            try:
                operation = int(op)
                curr_score += operation
                valid_rounds.append(operation)
            
            except ValueError:
                if op == "C":
                    operation = valid_rounds[-1] * -1
                    # ops.pop(ind-1)
                    valid_rounds.pop()
                    curr_score += operation
                if op == "D":
                    operation = 2 * valid_rounds[-1]
                    curr_score += operation
                    valid_rounds.append(operation)

                if op == "+":
                    operation = valid_rounds[-1] + valid_rounds[-2]
                    curr_score += operation
                    valid_rounds.append(operation)
            
        return curr_score
