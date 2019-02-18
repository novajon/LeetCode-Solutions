# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        #horizontal position
        h_pos = 0
        
        #vertical position
        v_pos = 0
        
        for inp in moves:
            if inp == "U":
                v_pos += 1
            elif inp == "D":
                v_pos -=1
            elif inp == "R":
                h_pos +=1
            else:
                h_pos-=1
        
        return v_pos == 0 and h_pos == 0
                
