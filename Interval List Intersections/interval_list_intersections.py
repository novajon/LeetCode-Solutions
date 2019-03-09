# https://leetcode.com/problems/interval-list-intersections/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        
        #a_pointer: pointer for input A to define which interval we are currently looking at
        a_pointer = 0
        #same for input B
        b_pointer = 0
        
        #store final intervals
        intervals = []
        
        #iterate through a and b until the end
        while a_pointer!= len(A) and b_pointer!=len(B):
            # if maximum of A interval is smaller than minimum of B interval
            if A[a_pointer].end < B[b_pointer].start:
                a_pointer += 1
            # if maximum of B interval is smaller than minimum of A interval
            elif A[a_pointer].start > B[b_pointer].end:
                b_pointer += 1
            else:
                intervals.append(Interval(max(A[a_pointer].start,B[b_pointer].start),min(A[a_pointer].end,B[b_pointer].end)))
                if A[a_pointer].end < B[b_pointer].end:
                    a_pointer+=1
                else:
                    b_pointer+=1
                
        return intervals
