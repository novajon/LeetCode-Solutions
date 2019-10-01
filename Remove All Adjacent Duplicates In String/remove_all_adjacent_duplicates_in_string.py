# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        
        ind = 0
        while ind < len(S):
            letter = S[ind]
            if stack and letter == stack[-1]:
                print("list")
                stack.pop()
                if ind+1 < len(S):
                    S = S[:ind-1] + S[ind+1:]
                else:
                    S = S[:ind-1]
                ind -= 1
            else:
                print("stack")
                stack.append(letter)
                ind += 1
        return S
        
